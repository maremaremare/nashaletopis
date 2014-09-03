from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from main.views import HomepageView, AboutView
import autocomplete_light
# import every app/autocomplete_light_registry.py
autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           HomepageView.as_view()),

                       # Examples:
                       # url(r'^$', 'nashaletopis.views.home', name='home'),
                       url(r'^stories/',
                           include('stories.urls', namespace='stories',)),
                       url(r'^radio/',
                           include('radio.urls', namespace='radio',)),
                       url(r'^map/',
                           include('helpmap.urls', namespace='helpmap',)),
                       url(r'^help/',
                           include('help.urls', namespace='help',)),
                       url(r'^aboutus',
                           AboutView.as_view(template_name='about.html')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^autocomplete/', include('autocomplete_light.urls')),
                       url(r'^captcha/', include('captcha.urls')),
                       url(r'^admin/', include('smuggler.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
if settings.DEBUG:
    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           url(r'',
                               include('django.contrib.staticfiles.urls')),
                           ) + urlpatterns

class Handler500(TemplateView):
    template_name = "500.html"  
    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view
handler500 = Handler500.as_error_view()