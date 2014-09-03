# -*- coding: utf-8 -*-
from django.db import models
from ordered_model.models import OrderedModel

# Create your models here.
class HelpItem(OrderedModel):
    title = models.CharField(max_length=100, help_text=u'Какая помощь нужна', verbose_name=u'Заголовок')
    slug = models.SlugField(help_text=u'Короткое имя для ссылки английскими буквами', verbose_name=u'Имя для адреса')
    description = models.CharField(max_length=300, help_text=u'Короткий подзаголовок. Его видно на главной странице', verbose_name=u'Описание')    
    text = models.TextField(help_text=u'Если копируется из word, нужно снять форматирование', verbose_name=u'Текст')
    icon = models.CharField(max_length=50, blank=True, null=True, help_text=u'Значок нужно выбрать по <a href="http://fortawesome.github.io/Font-Awesome/icons/" target="blank">этой ссылке</a>. В поле вписать его название без префикса "fa-"', verbose_name=u'Значок')
    

    def get_absolute_url(self):
        return '/help/{0}'.format(self.slug)

    class Meta(OrderedModel.Meta):
        verbose_name = ('Элемент "как помочь"')
        verbose_name_plural = ('Элементы "как помочь"')

    def __unicode__(self):
        return self.title
    