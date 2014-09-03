# -*- coding: utf-8 -*-
from django.db import models
#from stories.models import Story

# Create your models here.

class Radio_category(models.Model):
    title = models.CharField(max_length=100, help_text=u'Название категории радиопрограмм', verbose_name=u'Название')
    slug = models.SlugField(help_text=u'Короткое имя для ссылки английскими буквами', verbose_name=u'Имя для адреса')

    class Meta:
        verbose_name = ('Категория радиопрограмм')
        verbose_name_plural = ('Категории радиопрограмм')

    def get_absolute_url(self):
        return '/radio/{0}'.format(self.slug)

    def __unicode__(self):
        return self.title
    


class Radio(models.Model):

    date = models.DateField(help_text=u'Дата выхода в эфир', verbose_name=u'Дата')
    category = models.ForeignKey(Radio_category, help_text=u'Выберите нужную категорию', verbose_name=u'Категория')
    audio = models.FileField(upload_to='radio/', help_text=u'Файл в формате mp3', verbose_name=u'Аудио программы')
    text = models.TextField(help_text=u'Короткое описание передачи', verbose_name=u'Короткое описание')
    participants = models.CharField(max_length=50, blank=True, null=True, help_text=u'Если в программе участвовали люди, у которых нет своих историй на сайте, можно их добавить сюда через запятую (необязательно). Основные участники добавятся сами, по мере добавления историй на сайт', verbose_name=u'Дополнительные участники')
    fulltext = models.TextField(blank=True, null=True, verbose_name=u'Полный текст', help_text=u'Полный текст радиопрограммы. Необязательно. Если копируется из word, нужно снять форматирование')

    class Meta:
        verbose_name = ('Радиопрограмма')
        verbose_name_plural = ('Радиопрограммы')
        ordering = ['-date']

    def get_absolute_url(self):
        return '/radio/{0}/{1}'.format(self.category.slug, self.id)

    def __unicode__(self):
        return str(self.date)+': '+self.category.title


class Announcement_radio(models.Model):
    date = models.DateField(help_text=u'Предполагаемая дата выхода в эфир', verbose_name=u'Дата')
    title = models.CharField(max_length=50, help_text=u'Заголовок анонса',  verbose_name=u'Заголовок')
    text = models.TextField(help_text=u'Текст анонса. Если копируется из word, нужно снять форматирование', verbose_name=u'Текст')

    class Meta:
        verbose_name = ('Анонс')
        verbose_name_plural = ('Анонсы')

    def __unicode__(self):
        return self.title
