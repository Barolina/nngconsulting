from django.db import models

# Create your models here.
# Create your models here.
class NNGModel(models.Model):
    address = models.CharField(max_length=255, default='', null=True, verbose_name='краткий адрес')
    full_address = models.CharField(max_length=255, default='', null=True, verbose_name='полный адрес адрес')
    email = models.CharField(max_length=255, default='',null=True, verbose_name='email')
    telefons = models.CharField(max_length=255, default='',null=True, verbose_name='телефоны через запятую')
    text_context = models.CharField(max_length=255, default='',null=True, verbose_name='заголовок')
    context_context = models.CharField(max_length=255, default='',null=True, verbose_name='лозунг')
    company = models.TextField(default='', null=True, verbose_name='текст о компании')
    geografy = models.TextField(default='', null=True, verbose_name='текст о географии услуг')
    vkansii = models.TextField(default='', null=True, verbose_name='текст о вакансии')
    opit_zagolok = models.TextField(default='', null=True, verbose_name='Опыт заголовок')
    opit_text = models.TextField(default='', null=True, verbose_name='текст об опыте')
