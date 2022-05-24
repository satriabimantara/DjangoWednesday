from django.views import View
from django.shortcuts import render


class IndexView(View):
    template_name = 'index.html'
    context = {
        'title_page': 'Home',
        'subtitle_page': "Halaman Home Index"
    }

    def get(self, request, **params):
        self.context['content'] = 'GET dari Class View'
        return render(request, self.template_name, self.context)
