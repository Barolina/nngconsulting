from django.contrib import admin

# Register your models here.
from django_summernote.widgets import SummernoteWidget

from nng.nngconsulting.models import NNGModel, Practici
from django import forms


class PracticiAdminForm(forms.ModelForm):
    class Meta:
        model = Practici
        widgets = {
            'name': SummernoteWidget(),
            'note':  SummernoteWidget(),
        }
        fields = '__all__'



admin.site.register(NNGModel)


class PracticiAdmin(admin.ModelAdmin):
    form = PracticiAdminForm


admin.site.register(Practici, PracticiAdmin)
