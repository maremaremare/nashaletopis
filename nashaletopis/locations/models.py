# -*- coding: utf-8 -*-
import requests
import logging
import json
import xml.etree.ElementTree as ET
from django.db import models
from django_ymap.fields import YmapCoord
from django.utils.encoding import smart_str
from mptt.models import MPTTModel, TreeForeignKey


# Get an instance of a logger
logger = logging.getLogger('my')

from south.modelsinspector import add_introspection_rules
rules = [
    (
        (YmapCoord, ), [],
        {
            "start_query": ["start_query", {"default": None}],
            "size_width": ["size_width", {"default": 500}],
            "size_height": ["size_height", {"default": 500}],
            "null": ["null", {"default": False}],
            "blank": ["blank", {"default": False}],
        }
    ),
]

add_introspection_rules(rules, ["^django_ymap\.fields"])


class Location(MPTTModel):
    title = models.CharField(
        max_length=200, unique=True, help_text=u'Название населенного пункта. Должно быть уникальным. Если есть два места с одинаковым названием, в скобках указать область', verbose_name=u'Название места')
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children')

    address = YmapCoord(max_length=200, start_query=u'Россия',
                        size_width=500, size_height=500, null=True, blank=True, help_text=u'Найдите и выберите место на карте. Нужно поставить точку. Если нет точного адреса, поставьте точку посередине нужного населенного пункта', verbose_name=u'Выбор места на карте')

    def get_coords(self):
        coord_str = self.address
        coords = coord_str.replace(' ', '').split(',')
        newstr = ''
        for x in coords[::-1]:  # reverse for
            x = x[:9]
            newstr += ', ' + x

        return newstr[2:]

    class Meta:
        verbose_name = ('Место')
        verbose_name_plural = ('Места')

    def __unicode__(self):
        return self.title

    def get_parent_title(self):

        if self.address:
            payload = {'geocode': self.address,
                       'sco': 'latlong'}
        else:
            payload = {'geocode': self.title}
        r = requests.get('http://geocode-maps.yandex.ru/1.x/', params=payload)

        tree = ET.fromstring(smart_str(r.text))
        area_names_iterator = tree.iter(
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AdministrativeAreaName')

        listareas = []
        for x in area_names_iterator:
            listareas.append(x.text)
        #regionname = listareas[-1]
        title = listareas[0]  # subregionname

        return title

    def get_parents(self):

        if u'округ' in self.title:
            return None

        title = self.get_parent_title()

        region, created = Location.objects.get_or_create(
            title=title)

        return region

    def getparentcoords(self, title):
        payloadparent = {'geocode': title,
                         'format': 'json'}
        request = requests.get(
            'http://geocode-maps.yandex.ru/1.x/', params=payloadparent)

        d = json.loads(request.text)
        coord_str = d['response']['GeoObjectCollection'][
            'featureMember'][0]['GeoObject']['Point']['pos']

        coordss = coord_str.split(' ')
        newstr = ''
        for x in coordss[::-1]:  # reverse for
            x = x[:9]
            newstr += ', ' + x

        return newstr[2:]

    def save(self, *args, **kwargs):

        self.parent = self.get_parents()
        super(Location, self).save(*args, **kwargs)


from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Location)
def my_callback(sender, instance, *args, **kwargs):

    instance.address = instance.getparentcoords(instance.title)
