Ejecución de aplicaciones web python en apache2
===============================================

Crear una página web con Python (sin framework)
-----------------------------------------------

Aunque de forma general se utilizan distintos framework (el más popular es django) para el desarrollo de aplicaciones web con Python. En este apartado vamos a introducir los  conceptos necesarios para crear una página web desarrollada con python, servida por un servidor web Apache, sin utilizar ningún framework. Para ello es necesario conocer el concepto de WSGI (Web Server Gateway Interface), que es una especificación de una interface simple y universal entre los servidores web y las aplicaciones web o frameworks desarrolladas con python.

    * `Crear una página web con Python <http://www.josedomingo.org/pledin/2015/03/crear-una-pagina-web-con-python/>`_


Crear una página web con Python (con framework)
-----------------------------------------------

Estudiando el apartado anterior podemos llegar a la conclusión que la utilización de un framework facilita mucho la implementación de aplicaciones web escritas en python. Tenemos a nuestra disposición muchos framework, el más conocido y usado es django, pero tenemos otros menos complejos como bottle o flask. La lista de framework python: `Web Frameworks for Python <https://wiki.python.org/moin/WebFrameworks>`_.

Pero antes de ver la configuración de apache2 para servir aplicaciones web python con distintos framework, vamos a estudiar la herramienta ``virtualenv``.

**Utilización de un entorno virtual de python**

Hay que tener en cuenta que python es ampliamente utilizado por muchas aplicaciones GNU/Linux por lo que cuando se instalan paquetes de python más modernos o más antiguos de los que corresponden con la distribución GNU/Linux que se está utilizando, es muy recomendable hacerlo dentro de un entorno aislado que no afecte a la larga a las versiones correspondientes de los paquetes del sistema. Hay varias formas de hacer esto, en adelante vamos a explicar la forma de hacerlo con `Python Virtual Environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_. 

Instalamos los paquetes ``python-virtualenv`` y ``python-dev`` con un usuario privilegiado del sistema::

    $ apt-get install python-dev python-virtualenv

Creamos un entorno virtual para instalar las dependencias que necesitamos con un usuario con privilegios normales::

    $ virtualenv Python
    Running virtualenv with interpreter /usr/bin/python2
    New python executable in Python/bin/python2
    Also creating executable in Python/bin/python
    Installing setuptools, pip...done.

Lo que hemos hecho ha sido crear un entorno virtual de python en el directorio $HOME/Python en el que se han instalado todos los paquetes de python necesarios para poder utilizar Python pip dentro de ese entorno y que los paquetes de python se instalen en dicho directorio por un usuario normal sin afectar a los paquetes de python del sistema.

Cada vez que vayamos a utilizar los paquetes de python de este entorno virtual o queramos instalar algún paquete nuevo, debemos activarlo mediante la instrucción::

    usuario@oslo:~$ source ~/Python/bin/activate
    (Python)usuario@oslo:~$

Como vemos se indica en el prompt con el prefijo (Python) que estamos dentro del entorno virtual. Y ahora podemos realizar en nuestro entorno virtual las instalaciones que queramos:

    (Python)usuario@oslo:~$ pip install bottle requests

Cuando estemos dentro del entorno virtual de python y queramos salir basta con hacer::

    (Python)usuario@oslo:~$ deactivate
    usuario@oslo:~$


**Ejemplo 1: Despliegue de una aplicación web desarrollada con bottle**

En este primer ejemplo suponemos que hemos instalado ``bottle`` y las librerías python necesarias del repositorio oficial de debian. Por ejemplo tenemos la siguiente aplicación bottle::

    from bottle import route, run   

    @route('/hello')
    def hello():
        return "Hola mundo" 

    run(host='localhost', port=8080, debug=True)

Sabemos que si ejecutamos el anterior programa, se ejecutará un servidor web escuchando en el puerto 8080 y podremos acceder a comprobar la página. El servidor web que ejecuta python no está pensando para producción, sólo para desarrollos y pruebas. Por lo tanto si queremos que apache2 sirva esta aplicación tenemos que configurar apache2 (con el módulo WSGI) de la manera adecuada:

Necesitamos crear un fichero ``app.wsgi`` que facilita un objeto de tipo ``application``. Veamos el siguiente fichero ``/var/www/miapp/app.wsgi``::

    import os
    
    # Change working directory so relative paths (and template lookup) work again
    os.chdir(os.path.dirname(__file__)) 

    import bottle
    # ... build or import your bottle application here ...
    # Do NOT use bottle.run() with mod_wsgi
    application = bottle.default_app()

Y la configuración del Apache2 sería la siguiente::

    <VirtualHost *>
        ServerName www.example.com
        DocumentRoot /var/www

        WSGIDaemonProcess miapp user=www-data group=www-data processes=1 threads=5 python-path=/var/www/html/miapp
        WSGIScriptAlias / /var/www/miapp/app.wsgi 

        <Directory /var/www/miapp>
            WSGIProcessGroup miapp
            WSGIApplicationGroup %{GLOBAL}
            Require all granted
        </Directory>
    </VirtualHost>

.. warning::

    Ya no es necesario que la aplicación bottle ejecute un servidor web, por lo tanto es necesario eliminar la instrucción ``run`` del código.


**Ejemplo 2: Despliegue de una aplicación web desarrollada con django**

Hemos instalado el paquete django que tenemos en el repositorio oficial de debian jessie::

    $ apt-get install python-django
    $ django-admin version
    1.7.11

La versión actual de django es la 1.10, en el siguiente ejemplo usaremos un entrono virtual para trabajar con la última versión de django.

Creamos una nueva aplicación django::

    /var/www/html# django-admin startproject mysite

En el directorio ``mysite`` se han creado los ficheros y necesarios para desarrollar nuestra aplicación django, puedo ejecutar un servidor web para probar la aplicación de la siguiente manera:

    /var/www/html/mysite# python manage.py runserver 0.0.0.0:8000
    
    Django version 1.7.11, using settings 'mysite.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.

Después de construir nuestra aplicación, si queremos desplegarla sobre apache2, tenemos que utilizar el fichero ``/var/www/html/mysite/mysite/wsgi.py`` y configurar apache2 de la siguiente manera::

    <VirtualHost *>
        ServerName www.example.com
        DocumentRoot /var/www/html/mysite
        WSGIDaemonProcess mysite user=www-data group=www-data processes=1 threads=5 python-path=/var/www/html/mysite
        WSGIScriptAlias / /var/www/html/mysite/mysite/wsgi.py

        <Directory /var/www/html/mysite>
                WSGIProcessGroup mysite
                WSGIApplicationGroup %{GLOBAL}
                Require all granted
        </Directory>
    </VirtualHost>

**Ejemplo 3: Despliegue de una aplicación web desarrollada con django usuando virtualenv**

Como hemos dicho en el ejemplo anterior si queremos utilizar la última versión de django tenemos que instalarlo en un  entrono virtual, para ello::

    $ virtualenv django
    $ source django/bin/activate
    (django)debian@python:~$  pip install django

Crearíamos nuestra aplicación djngo y a la hora de modificar la configuración de apache2 la única línea que tendríamos que modificar sería la siguiente::

    ...
    WSGIDaemonProcess mysite user=www-data group=www-data processes=1 threads=5 python-path=/var/www/html/mysite:/home/debian/python/lib/python2.7/site-packages
    ...

teniendo en cuenta que el entorno virtual python lo hicimos en el directorio ``/home/debian/python``.