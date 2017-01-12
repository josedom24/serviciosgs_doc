Ejecución de aplicaciones web python en apache2
===============================================

Crear una página web con Python (sin framework)
-----------------------------------------------

Aunque de forma general se utilizan distintos framework (el más popular es django) para el desarrollo de aplicaciones web con Python. En este apartado vamos a introducir los  conceptos necesarios para crear una página web desarrollada con python, servida por un servidor web Apache, sin utilizar ningún framework. Para ello es necesario conocer el concepto de WSGI (Web Server Gateway Interface), que es una especificación de una interface simple y universal entre los servidores web y las aplicaciones web o frameworks desarrolladas con python.

    * `Crear una página web con Python <http://www.josedomingo.org/pledin/2015/03/crear-una-pagina-web-con-python/>`_


Crear una página web con Python (con framework)
-----------------------------------------------

Estaudiando el apartado anterior podemos llegar a la conclusión que la utilización de un framework facilita mucho la implementación de aplicaciones web escritas en python. Tenemos a nuestra disposición muchos framework, el más conocido y usado es django, pero tenemos otros menos complejos como bottle o flask. La lista de framework python: `Web Frameworks for Python <https://wiki.python.org/moin/WebFrameworks>`_.

Pero antes de ver la configuración de apache2 para servir aplicaciones web python con distintos framework, vamos a estudiar la herrmienta virtualenv.

**Utilización de un entorno virtual de python**

Hay que tener en cuenta que python es ampliamente utilizado por muchas aplicaciones GNU/Linux por lo que cuando se instalan paquetes de python más modernos o más antiguos de los que corresponden con la distribución GNU/Linux que se está utilizando, es muy recomendable hacerlo dentro de un entorno aislado que no afecte a la larga a las versiones correspondientes de los paquetes del sistema. Hay varias formas de hacer esto, en adelante vamos a explicar la forma de hacerlo con `Python Virtual Environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_. 

Instalamos los paquetes ``python-virtualenv`` y ``python-dev`` con un usuario privilegiado del sistema::

    apt-get install python-dev python-virtualenv

Creamos un entorno virtual para instalar las dependencias que necesitamos con un usuario con privilegios normales::

    virtualenv Python
    Running virtualenv with interpreter /usr/bin/python2
    New python executable in Python/bin/python2
    Also creating executable in Python/bin/python
    Installing setuptools, pip...done.

Lo que hemos hecho ha sido crear un entorno virtual de python en el directorio $HOME/Python en el que se han instalado todos los paquetes de python necesarios para poder utilizar Python pip dentro de ese entorno y que los paquetes de python se instalen en dicho directorio por un usuario normal sin afectar a los paquetes de python del sistema.

Cada vez que vayamos a utilizar los paquetes de python de este entorno virtual o queramos instalar algún paquete nuevo, debemos activarlo mediante la instrucción::

    usuario@oslo:~$ source ~/Python/bin/activate
    (Python)usuario@oslo:~$

Como vemos se indica en el prompt con el prefijo (Python) que estamos dentro del entorno virtual.

Cuando estemos dentro del entorno virtual de python y queramos salir basta con hacer::

    (Python)usuario@oslo:~$ deactivate
    usuario@oslo:~$



























**Módulo php de Apache2**

Módulo de apache: libapache2-mod-php5. Para más información: `Instalación de php en Debian <http://php.net/manual/es/install.unix.debian.php#install.unix.debian>`_. El fichero de configuración de php lo encontramos en ``/etc/php5/apache2/php.ini``, para más información sobre la configuración: `How To Change Your PHP Settings on Ubuntu 14.04  <https://www.digitalocean.com/community/tutorials/how-to-change-your-php-settings-on-ubuntu-14-04>`_

Si usuas el módulo de PHP de apache2 no podrás utilizar los MPM *event* ni *worker*, se configurará de forma automática en **prefork**.

**CGI**

La ejecución del código php se hace por un proceso independiente del servidor web. Hay distintas alternativas: CGI, Fastcgi, PHP-FPM,…, puedes ver las diferencias en este `enlace <http://serverfault.com/questions/645755/differences-and-dis-advanages-between-fast-cgi-cgi-mod-php-suphp-php-fpm>`_.

	* FastCGI es un protocolo para interconectar programas interactivos con un servidor web. FastCGI es una variación de la ya conocida Common Gateway Interface (CGI ó Interfaz Común de Entrada). El principal objetivo de FastCGI es reducir la carga asociada con el hecho de interconectar el servidor web y los programas Common Gateway Interface, permitiéndole a un servidor atender más peticiones a la vez.
	* FPM (`FastCGI Process Manager <http://php.net/manual/es/install.fpm.php>`_) es una implementación alternativa al PHP FastCGI con algunas características adicionales (la mayoría) útiles para sitios web con mucho tráfico.
    * `Apache 2.4 with php5-fpm <https://www.digitalocean.com/community/questions/apache-2-4-with-php5-fpm>`_

**Aceleradores PHP**

El objetivo principal de un acelerador PHP es guardar los scripts php ya compilando, obteniendo un mayor rendimiento en la respuesta del servidor. El acelerador se puede usar usando el módulo php de apache o usando fastcgi. Más información sobre `aceleradores PHP <http://www.maestrosdelweb.com/aceleradores-de-php/>`_.

En la última versión de php (PHP 5.5) ya tenemos una cache de código instalada como módulo. En la documentación de PHP 5.5 podemos leer: *“La caché de códigos de operación de Zend Optimiser+ se ha añadido a PHP como la nueva extensión OPcache. OPcache mejora el rendimiento de PHP almacenando código de byte de un script precompilado en la memoria compartida, eliminando así la necesidad por parte de PHP de cargar y analizar scripts en cada petición.”*

Además tenemos otro módulo instalado en PHP 5.5, el módulo ``apcu``, que permite a PHP guardar cierta información en memoria, por lo que también podemos acelerar el proceso de interpretación de código. Para más información sobre estos dos módulos de php puedes leer el artículo: `PHP 5.5 with Opcache and APCu <http://jessesnet.com/development-notes/2014/php-55-opcache-apcu/>`_

**Memcached**

`Memcached <http://memcached.org/>`_ es un sistema distribuido de propósito general y que es muy usado en la actualidad por múltiples sitios web. Memcached es empleado para el almacenamiento en caché de datos u objetos en la memoria RAM, reduciendo así las necesidades de acceso a un origen de datos externo (como una base de datos o una API).

    * `Manual de instalación de memcached <http://www.pontikis.net/blog/install-memcached-php-debian>`_
    * `Como utilizar Memcached con WordPress <https://raiolanetworks.es/blog/como-utilizar-memcached-con-wordpress/>`_

**Varnish**

Varnish es un acelerador HTTP que funciona como un proxy inverso. Se sitúa por delante del servidor web, cacheando la respuesta de dicho servidor web en memoria. La próxima vez que un visitante visite la misma URL, la página será servida desde Varnish en lugar de desde el servidor web, ahorrando recursos en el backend y permitiendo más conexiones simultáneas.

    * `Presentación Madrid DevOps (Varnish: funcionamiento, configuración y uso) <http://www.youtube.com/watch?v=A5poVWqjJrs>`_
    * `http://pabloroman.es/blog/2013/01/20/como-usar-varnish-para-acelerar-tu-sitio-web/ <http://pabloroman.es/blog/2013/01/20/como-usar-varnish-para-acelerar-tu-sitio-web/>`_
    * `How to: Varnish listen port 80 with systemd <http://deshack.net/how-to-varnish-listen-port-80-systemd/>`_
    * `http://pabloroman.es/blog/2013/05/20/varnish-3-trucos-y-consejos/ <http://pabloroman.es/blog/2013/05/20/varnish-3-trucos-y-consejos/>`_
    * `https://scalr-wiki.atlassian.net/wiki/display/docs/Install+Varnish+HTTP+Accelerator+with+WordPress <https://scalr-wiki.atlassian.net/wiki/display/docs/Install+Varnish+HTTP+Accelerator+with+WordPress>`_
    * `http://kontsu.wordpress.com/2012/10/10/apache-2-performance-boost-with-varnish-yslow/ <http://kontsu.wordpress.com/2012/10/10/apache-2-performance-boost-with-varnish-yslow/>`_
     * `Put Varnish on port 80 <http://www.varnish-cache.org/docs/trunk/tutorial/putting_varnish_on_port_80.html>`_
