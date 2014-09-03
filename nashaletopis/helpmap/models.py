# -*- coding: utf-8 -*-
from django.db import models
from locations.models import Location
from mptt.models import TreeForeignKey
# Create your models here.


class HelpingCategory(models.Model):
    title = models.CharField(max_length=100, help_text=u'Название категории помогающих организаций', verbose_name=u'Название')
    slug = models.SlugField(help_text=u'Короткое имя для ссылки английскими буквами', verbose_name=u'Имя для адреса')

    class Meta:
        verbose_name = ('Категория помогающих организаций')
        verbose_name_plural = ('Категории помогающих организаций')

    def get_absolute_url(self):
        return '/map/helpgiven/{0}'.format(self.slug)

    def __unicode__(self):
        return self.title


class HelpingOrganisation(models.Model):
    title = models.CharField(max_length=200, help_text=u'Название организации', verbose_name=u'Название')
    category = models.ForeignKey(HelpingCategory, help_text=u'Выберите нужную категорию', verbose_name=u'Категория')
    location = TreeForeignKey(Location, related_name='helpgiven', help_text=u'Выберите или создайте место на карте', verbose_name=u'Место')
    address = models.CharField(max_length=300, help_text=u'Полный адрес', verbose_name=u'Адрес')
    text = models.TextField(blank=True, null=True, help_text=u'Об организации. Если копируется из word, нужно снять форматирование', verbose_name=u'Об организации')
    phone = models.CharField(max_length=50, help_text=u'Введите телефон (можно несколько через запятую)', verbose_name=u'Телефон')
    email = models.EmailField(blank=True, null=True, help_text=u'Если есть электронная почта, можно указать ее здесь', verbose_name=u'E-mail')
    site = models.URLField(blank=True, null=True, help_text=u'Если есть сайт, ссылку можно указать здесь', verbose_name=u'Адрес сайта')
    opened = True
    class Meta:
        verbose_name = ('Помогающая организация')
        verbose_name_plural = ('Помогающие организации')

    def get_absolute_url(self):
        return '/map/helpgiven/{0}/{1}'.format(self.location.id, self.id)

    def __unicode__(self):
        return self.title


class HelpNeeded(models.Model):
    title = models.CharField(max_length=200, help_text=u'Название организации', verbose_name=u'Название')
    text = models.TextField(help_text='Если копируется из word, нужно снять форматирование', verbose_name=u'Текст')
    link = models.URLField(help_text='Ссылка - куда обратиться, если хочешь помочь', verbose_name=u'Ссылка')
    location = TreeForeignKey(Location, related_name='helpneeded', help_text=u'Выберите или создайте место на карте', verbose_name=u'Место')
    opened = models.BooleanField(default=True, help_text='Чтобы закрыть просьбу, снимите галку', verbose_name=u'Открыто?')

    class Meta:
        verbose_name = ('Просьба о помощи')
        verbose_name_plural = ('Просьбы о помощи')

    def get_absolute_url(self):
        return '/map/helpneeded/{0}/{1}'.format(self.location.id, self.id)

    def __unicode__(self):
        return self.title
