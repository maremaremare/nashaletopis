
from django.views.generic import TemplateView, ListView
from stories.models import Story, History_period
from radio.models import Radio
from helpmap.models import HelpNeeded, HelpingOrganisation
from help.models import HelpItem
from main.models import TeamMember


class HomepageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['latest_stories'] = Story.objects.filter(is_photo_shown=True)
        context['latest_radio'] = Radio.objects.all()[:6]
        context['helpus'] = HelpItem.objects.all()[:4]
        context['helpneeded'] = HelpNeeded.objects.all()
        context['helpgiven'] = HelpingOrganisation.objects.all()
        context['periods'] = History_period.objects.all()
        return context


class AboutView(ListView):
    template_name = 'about.html'
    model = TeamMember