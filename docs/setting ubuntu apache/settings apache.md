# Настройки применяемы на сайте

1. Установка и натрока **Apache** and **ufw**
 
 - [установить веб-сервер Apache на Ubuntu 16.04](https://timeweb.com/ru/community/articles/kak-ustanovit-veb-server-apache-na-ubuntu-16-04-1)
 - [установка Python, Django, настройка Apache, доступ к базе sqllite](https://www.8host.com/blog/obsluzhivanie-prilozhenij-django-s-pomoshhyu-apache-i-mod_wsgi-v-ubuntu-16-04/) 
 - [активация и деактивация conf файла Apache](https://freaksense.com/how-to-configure-apache-virtual-hosts-on-ubuntu/)
 - [Django pytohn3.5 add user for Apache and Postgres deploy ](https://pythoness.pp.ua/catalog/article/razvorachivanie-django-proekta-na-ubuntu-16/)
 - [Как настроить виртуальные хосты в Apache на Ubuntu 16.04 ](https://www.digitalocean.com/community/tutorials/apache-ubuntu-16-04-ru)
   
   '''
     
        sudo a2ensite example2.com.conf
        
        sudo a2ensite example2.com.conf
        
        sudo systemctl restart apache2 
   '''
 - активация ssl in apapche
   
        sudo a2enmod ssl

 - [Настройка HTTPS в Apache (ssl)](http://help.ubuntu.ru/wiki/apache_%D0%B8_https)
   
   или
 
 - [Установка SSL-сертификата на Apache (Linux)](https://1cloud.ru/help/ssl/installsslapache)
 
 - [Описание Django хостинг](http://nowhereland.ru/django-hosting/#.WmEOTDeYO02)
  
 - [Djnago .httaccess](https://www.ibm.com/developerworks/ru/library/os-django/index.html)
 -  
   
## Django error  Pillow not found hassatr

   
    
        sudo pip3 uninstall pil
        
        sudo pip3 uninstall pillow
        
        sudo pip3 install pillow
      
### Apache получить последние 10 строк лога

        sudo tail -f /var/log/apache2/error.log
        
### Как указать в Apache Env Django

          # Envvars for Django aplication 'Prehranske oznacbe'.
          SetEnv DJANGO_SETTINGS_MODULE prehranske_oznacbe.settings.production
          SetEnv OZNACBE_API_USERNAME (redacted)
          SetEnv OZNACBE_API_PASSWORD (redacted)
          SetEnv OZNACBE_SECRET_KEY (redacted)
         
### Как проверить, какие порты слушаются какими программами в linux
        netstat -plutn
        
          
### [Git шпаргалка](http://programilla.com/blog/siteconstruction/325.html)

### Примеры разворота на продакш

    - [Разворачивание Django-проекта на Ubuntu 16- ngix](https://pythoness.pp.ua/catalog/article/razvorachivanie-django-proekta-na-ubuntu-16/)
    - [Django на Ubuntu с Apache и mod_wsgi and Mysql кратко команды](http://materynko.blogspot.ru/2011/06/django-ubuntu-apache-modwsgi.html)
    
### [Повышаем безопасность сайта при помощи .htaccess](http://www.securityscripts.ru/articles/%D0%9E%D0%B1%D1%89%D0%B5%D0%B5/security-site-htaccess.html)

        
### [дешевый VPS](https://firstvds.ru/?from=96322&utm_expid=.00laGFGKRe2v_KwJ6X9aQw.0&utm_referrer=https%3A%2F%2Fhabrahabr.ru%2Fpost%2F159575%2F) 
