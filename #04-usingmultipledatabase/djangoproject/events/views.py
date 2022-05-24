from django.shortcuts import render
from django.views import View
# Create your views here.


class IndexView(View):
    template_name = 'events/index.html'
    context = {
        'title_page': 'Home Event',
        'subtitle_page': 'Halaman Event Index'
    }

    def get(self, request, **params):
        self.context['content'] = 'GET dari Class View Event'
        return render(request, self.template_name, self.context)
