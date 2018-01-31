from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from nng.nngconsulting.models import NNGModel, Practici


def _index(request):
    return HttpResponse('est')

class index(ListView):
    queryset = NNGModel.objects.first()
    template_name = 'index.html'
    context_object_name = 'obj'

    def get_queryset(self):
        # res = super(index,self).get_queryset(self)
        print(self.queryset)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['practic'] = Practici.objects.all()
        return context


class practic(ListView):
    queryset = Practici.objects.all()
    template_name = 'practic.html'
    context_object_name = 'prc'

    def get_queryset(self):
        # res = super(index,self).get_queryset(self)
        print(self.queryset)
        return self.queryset


class practicDetailView(DetailView):
        model = Practici
