# -*- coding: utf-8 -*-
from .models import Mainpage
from radio.models import Announcement_radio
from stories.models import Story
import random

def write_context(request):
    return {'main': Mainpage.objects.get(id=1), 'radio_a': Announcement_radio.objects.all()[:2], 'faces': sorted(Story.objects.filter(is_photo_shown=True)[:9], key=lambda x: random.random())}
