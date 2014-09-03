# -*- coding: utf-8 -*-
from django.db import models
from solo.models import SingletonModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Anchor
# Create your models here.


class Mainpage(SingletonModel):

    title = models.CharField(max_length=200, help_text=u'Название сайта. Его видно на всех страницах', verbose_name=u'Название сайта')
    subtitle = models.CharField(max_length=200, help_text=u'Подзаголовок. Его видно на всех страницах', verbose_name=u'Подзаголовок сайта')
    our_mission = models.TextField(help_text=u'Этот текст начинается на главной странице и продолжается на собственной странице "О проекте"', verbose_name=u'О проекте')
    address = models.CharField(max_length=200, blank=True, null=True, help_text=u'Будет показан в контактах', verbose_name=u'Адрес')
    email = models.EmailField(max_length=50, blank=True, null=True, help_text=u'Будет показан в контактах', verbose_name=u'Email')
    phone = models.CharField(max_length=50, blank=True, null=True, help_text=u'Будет показан в контактах', verbose_name=u'Телефон')
    skype = models.CharField(max_length=50, blank=True, null=True, help_text=u'Будет показан в контактах', verbose_name=u'Скайп')

    hotline = models.CharField(max_length=50, help_text=u'Введите сюда номер телефона горячей линии', verbose_name=u'Телефон горячей линии')

    is_social_shown = models.BooleanField(default=True, help_text=u'Отметьте, если хотите показывать соцсети. Они будут показаны на всех страницах в самом низу', verbose_name=u'Показывать соцсети?')
    is_hotline_shown = models.BooleanField(default=True, help_text=u'Отметьте, если хотите, чтобы горячая линия была показана', verbose_name=u'Показывать горячую линию?')
    are_latest_stories_shown = models.BooleanField(default=True, help_text=u'Отметьте, если хотите, чтобы "последние истории" были показаны на главной странице', verbose_name=u'Показывать последние истории (темный блок с фото и текстом)?')
    is_photoalbum_shown = models.BooleanField(default=True, help_text=u'Отметьте, если хотите, чтобы фотоальбом был показан на главной странице', verbose_name=u'Показывать фотоальбом ("лоскутное одеяло")?')
    is_map_shown = models.BooleanField(default=True, help_text=u'Отметьте, если хотите, чтобы карта была показана на главной странице', verbose_name=u'Показывать карту?')


    facebook = models.URLField(null=True, blank=True, verbose_name=u'Фейсбук')
    vkontakte = models.URLField(null=True, blank=True, verbose_name=u'ВКонтакте')
    twitter = models.URLField(null=True, blank=True, verbose_name=u'Твиттер')
    instagram = models.URLField(null=True, blank=True, verbose_name=u'Инстаграмм')
    livejournal = models.URLField(null=True, blank=True, verbose_name=u'Живой Журнал')

    class Meta:
        verbose_name = ('Главная страница и настройки сайта')
        verbose_name_plural = ('Главная страница и настройки сайта')

    def __unicode__(self):
        return u'Главная страница и настройки сайта'

class TeamMember(models.Model):
    name = models.CharField(max_length=150, verbose_name=u'Имя')
    job = models.CharField(max_length=200, verbose_name=u'Должность')
    about = models.TextField(verbose_name=u'Про человека и его работу')
    photo = models.ImageField(upload_to='photos/team/', verbose_name=u'Фото')

    thumbnail = ImageSpecField(source='photo',
                                    processors=[ResizeToFill(250, 250)],
                                    format='JPEG',
                                    options={'quality': 60})

    class Meta:
        verbose_name = ('Член команды')
        verbose_name_plural = ('Члены команды')

    def __unicode__(self):
        return self.name
    
