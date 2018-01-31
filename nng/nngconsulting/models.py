#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
# Create your models here.
from django.urls import reverse
from tinymce.models import HTMLField


class NNGModel(models.Model):
    address = models.CharField(max_length=255, default='', null=True, verbose_name=u"краткий адрес")
    full_address = models.CharField(max_length=255, default='', null=True, verbose_name=u"полный адрес адрес")
    email = models.CharField(max_length=255, default='',null=True, verbose_name=u"email")
    telefons = models.CharField(max_length=255, default='',null=True, verbose_name=u"телефоны через запятую")
    text_context = models.CharField(max_length=255, default='',null=True, verbose_name=u"заголовок")
    context_context = models.CharField(max_length=255, default='',null=True, verbose_name=u"лозунг")
    company = models.TextField(default='', null=True, verbose_name=u"текст о компании")
    geografy = models.TextField(default='', null=True, verbose_name=u"текст о географии услуг")
    vkansii = models.TextField(default='', null=True, verbose_name=u"текст о вакансии")
    opit_zagolok = models.TextField(default='', null=True, verbose_name=u"Опыт заголовок")
    opit_text = models.TextField(default='', null=True, verbose_name=u"текст об опыте")

class Practici(models.Model):
    name = HTMLField()
    note = HTMLField()

    class Meta:
        verbose_name = 'Описание практис'

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('nng:practic-detail', args=[str(self.id)])
