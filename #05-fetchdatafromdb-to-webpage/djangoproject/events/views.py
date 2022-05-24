from django.shortcuts import render
from django.views import View
from .models import Event
# Create your views here.


class IndexView(View):
    template_name = 'events/index.html'
    context = {
        'title_page': 'Home Event',
        'subtitle_page': 'Halaman Event Index'
    }

    def get(self, request, **params):
        event_list = Event.objects.all()
        self.context['event_list'] = event_list
        return render(request, self.template_name, self.context)
