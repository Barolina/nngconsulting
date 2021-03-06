"""
WSGI config for nng project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys


# #путь к проекту
# <<<<<<< HEAD
# =======
#<<<<<<< HEAD
#<<<<<<< HEAD
#from django.core.wsgi import get_wsgi_application

#=======
#>>>>>>> b5b30be483cb6abf23e10e5aecd46ad928b83b63
#=======
#>>>>>>> 343e98302129f3cd61cdf9538b009330f8bfb212

#путь к проекту
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/www-root/data/www/nngconsulting.com/nngconsulting')
#путь к фреймворку
sys.path.insert(0, '/var/www/www-root/data/www/nngconsulting.com/')
#путь к виртуальному окружению
sys.path.insert(0, '/var/www/nngconsulting.com/venv/lib/python3.5/site-packages/')


# This allows easy placement of apps within the interior
# nng directory.
app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
sys.path.append(os.path.join(app_path, 'nng'))



#if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
#    from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.production"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()
#if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
#    application = Sentry(application)
# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)




