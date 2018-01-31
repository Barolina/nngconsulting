from django.contrib import admin

# Register your models here.
from nng.nngconsulting.models import NNGModel, Practici




class NNGModelAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form.html'

admin.site.register(NNGModel, NNGModelAdmin)


class PracticiAdmin(admin.ModelAdmin):
    change_form_template = 'admin/change_form.html'

admin.site.register(Practici, PracticiAdmin)
