# -*- coding: utf-8 -*-
import autocomplete_light
from .models import Radio

# This will generate a PersonAutocomplete class
autocomplete_light.register(Radio,
    # Just like in ModelAdmin.search_fields
    search_fields=['date', 'category__title'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': u'Начните вводить дату радиопередачи',
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