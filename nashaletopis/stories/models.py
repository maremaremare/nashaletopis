# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Anchor
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager
from taggitcyr.models import TaggedItemCyrillic
from radio.models import Radio
from locations.models import Location
from mptt.models import TreeForeignKey
from .widgets import MPTTModelMultipleChoiceField



class History_period(MPTTModel):
    name = models.CharField(max_length=50, unique=True, help_text=u'Название исторического периода', verbose_name=u'Название')
    slug = models.SlugField(help_text=u'Короткое имя для ссылки английскими буквами и цифрами', verbose_name=u'Имя для адреса')
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children', help_text=u'Выберите родителя (необязательно)', verbose_name=u'Родитель')

    class Meta:
        verbose_name = ('Период истории')
        verbose_name_plural = ('Периоды истории')

    def get_absolute_url(self):
        return '/stories/period/{0}'.format(self.slug)

    def __unicode__(self):

        name = ''
        for item in self.get_ancestors(include_self=True):
            name += ' - ' + item.name
        return name[2:]

# Create your models here.


class Story(models.Model):

    name = models.CharField(max_length=100, help_text=u'Имя человека и заголовок истории', verbose_name=u'Имя')
    birthyear = models.IntegerField(blank=True, null=True, help_text=u'Год рождения, цифрами', verbose_name=u'Год рождения')
    text = models.TextField(help_text=u'Текст истории. Если копируется из word, нужно снять форматирование', verbose_name=u'Текст')
    period = models.ManyToManyField(
        History_period, blank=True, null=True, related_name='stories', verbose_name=u'Период истории', help_text=u'Выберите нужный период',)
    location = models.ManyToManyField(Location, related_name='stories', help_text=u'Можно выбрать несколько', verbose_name=u'Место', blank=True, null=True)
    radioprogram = models.ForeignKey(Radio, blank=True, null=True, help_text=u'Связанная аудиопрограмма. Необязательно', verbose_name=u'Аудиопрограмма')
    audio = models.FileField(upload_to='story_audio/', blank=True, null=True, help_text=u'Файл в формате mp3', verbose_name=u'Аудиозапись истории')
    tags = TaggableManager(through=TaggedItemCyrillic, blank=True, verbose_name=u'Метки')
    is_letter = models.BooleanField(help_text=u'Если это письмо, отметьте здесь', verbose_name=u'Это письмо?')
    is_photo_shown = models.BooleanField(default=True, help_text=u'Если нужно убрать фото с обложки, снимите галку', verbose_name=u'Показывать фото на обложке?')

    def get_absolute_url(self):
        return '/stories/read/{0}'.format(self.id)

    def get_locations(self):
        return "\n".join([p.title for p in self.location.all()])

    get_locations.short_description = u'Места'

    def get_periods(self):
        return "\n".join([p.name for p in self.period.all()])

    get_periods.short_description = u'Периоды истории'

    class Meta:
        verbose_name = ('История')
        verbose_name_plural = ('Истории')

    def __unicode__(self):
        return self.name



class StoryActive(models.Model):

    name = models.CharField(max_length=100, help_text=u'Имя человека и заголовок истории', verbose_name=u'Имя')
    birthyear = models.IntegerField(blank=True, null=True, help_text=u'Год рождения, цифрами', verbose_name=u'Год рождения')
    text = models.TextField(help_text=u'Текст истории. Если копируется из word, нужно снять форматирование', verbose_name=u'Текст')
    location = TreeForeignKey(
        Location, related_name='stories_active', null=True, help_text=u'Выберите место', verbose_name=u'Место')
    radioprogram = models.ForeignKey(
        Radio, blank=True, null=True, related_name='stories', help_text=u'Связанная аудиопрограмма. Необязательно', verbose_name=u'Аудиопрограмма')
    audio = models.FileField(upload_to='story_audio/', blank=True, null=True, help_text=u'Файл в формате mp3', verbose_name=u'Аудиозапись истории')
    tags = TaggableManager(through=TaggedItemCyrillic, blank=True, verbose_name=u'Метки')
    is_letter = models.BooleanField(help_text=u'Если это письмо, отметьте здесь', verbose_name=u'Это письмо?')
    is_photo_shown = models.BooleanField(default=True, help_text=u'Если нужно убрать фото с обложки, снимите галку', verbose_name=u'Показывать фото на обложке?')


    def get_absolute_url(self):
        return '/stories/active/read/{0}'.format(self.id)

    class Meta:
        verbose_name = ('История - активное долголетие')
        verbose_name_plural = ('Истории - активное долголетие')

    def __unicode__(self):
        return self.name


class Photo(models.Model):

    photo = models.ImageField(upload_to='photos/', help_text=u'Фото в формате .jpg', verbose_name=u'Файл')
    description = models.CharField(null=True, blank=True, max_length=300, help_text=u'Описание фотографии (необязательно)', verbose_name=u'Описание')
    story = models.ForeignKey(
        Story, null=True, blank=True, related_name='photos')
    activestory = models.ForeignKey(
        StoryActive, null=True, blank=True, related_name='photos')
    storylist_thumbnail = ImageSpecField(source='photo',
                                         processors=[ResizeToFit(150, 150)],
                                         format='JPEG',
                                         options={'quality': 60})
    storydetail_thumbnail = ImageSpecField(source='photo',
                                           processors=[ResizeToFit(300, 300)],
                                           format='JPEG',
                                           options={'quality': 60})
    gallery_thumbnail = ImageSpecField(source='photo',
                                       processors=[ResizeToFill(834, 834)],
                                       format='JPEG',
                                       options={'quality': 60})
    homepage_thumbnail = ImageSpecField(source='photo',
                                        processors=[ResizeToFill(276, 276)],
                                        format='JPEG',
                                        options={'quality': 60})
    photoalbum_thumbnail = ImageSpecField(source='photo',
                                          processors=[ResizeToFill(230, 230)],
                                          format='JPEG',
                                          options={'quality': 60})
    footer_thumbnail = ImageSpecField(source='photo',
                                          processors=[ResizeToFill(73, 73)],
                                          format='JPEG',
                                          options={'quality': 60})

    class Meta:
        verbose_name = ('Фотография')
        verbose_name_plural = ('Фотографии')
        ordering = ['photo']
        

    def __unicode__(self):
        if self.story:
            name = self.story.name
        if self.activestory:
            name = self.activestory.name
        return str(self.id) + ' ' + name


class Video(models.Model):

    title = models.CharField(help_text=u"Название", max_length=50, verbose_name=u'Название')
    video = EmbedVideoField(help_text=u"Ссылка на видео в youtube (видео нужно закачать на <a href='http://youtube.com' target='blank'>Ютуб</a>)", verbose_name=u'Видео')
    story = models.ForeignKey(
        Story, null=True, blank=True, related_name='videos')
    activestory = models.ForeignKey(StoryActive, null=True, blank=True)

    class Meta:
        verbose_name = ('Видео')
        verbose_name_plural = ('Видео')

    def __unicode__(self):
        return self.title
