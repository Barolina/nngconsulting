from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from nng.nngconsulting.models import NNGModel


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
