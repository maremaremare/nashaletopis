# -*- coding: utf-8 -*-
import autocomplete_light
from .models import Location
from taggit.models import Tag
from stories.models import History_period

autocomplete_light.register(Tag)

# This will generate a PersonAutocomplete class
autocomplete_light.register(Location,
    # Just like in ModelAdmin.search_fields
    search_fields=['title'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': u'Начните вводить название населенного пункта или области',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)


autocomplete_light.register(History_period,
    # Just like in ModelAdmin.search_fields
    search_fields=['name'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': u'Начните вводить название периода',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)