Ejercicio: Instalación y configuración básica de Apache
=======================================================

Instalación de Apache 2.2
-------------------------

1. Instala el servidor web Apache e indica el FQDN para que al inciar el servicio no nos de ningún problema.

Para controlar el servicio apache2 podemos usar: (para más información <http://httpd.apache.org/docs/2.2/es/stopping.html>)::

    apache2ctl [-k start|restart|graceful|graceful-stop|stop]

2. ¿Qué es la opción graceful?

3. Comprueba la directiva donde indicamos el puerto de escucha del servidor. Modifica el puerto de escucha para que sea el 8080. Comprueba el acceso al servidor desde un navegador.

4. Comprueba los módulos  cargados en el servidor.

5. Comprueba los sitios webs activos en nuestro servidor.

Estructura de los ficheros de configuración
-------------------------------------------

1. Las directivas de configuración de apache2 se pueden aplicar si está definido un determinado parámetro. Para esto se utiliza la directiva * `IfDefine <http://httpd.apache.org/docs/2.2/mod/core.html#ifdefine>`_. Busca en algún fichero de configuración esta directiva.

2. Igualmente podemos aplicar determinadas directivas si hay cargado un determinado módulo, para ello usamos `IfModule <http://httpd.apache.org/docs/2.2/mod/core.html#ifmodule>`_. Busca alguna directiva de este tipo.

Para cargar dinámicamente los módulos se utilza la directiva `LoadModule <http://httpd.apache.org/docs/2.4/mod/mod_so.html#loadmodule>`_, búscalos en los ficheros .load dentro de ``/etc/apache2/mods-availables``.

Más información: http://httpd.apache.org/docs/2.4/dso.html

3. Busca en la configuración una variable de entorno y determina en que fichero están definidas.

4. La directiva `Include <http://httpd.apache.org/docs/2.2/mod/core.html#include>`_
 nos permite añadir ficheros de configuración a la configuración general de apache2. Comprueba qué ficheros son añadidos con esta directiva.

5. Podemos aplicar directivas a partes concretas de nuestro servidor web, para ello estudia las siguientes directivas (Para aprender más lee `Secciones de Configuración <http://httpd.apache.org/docs/2.2/sections.html>`_):

* `Directory <http://httpd.apache.org/docs/2.2/mod/core.html#directory>`_
* `DirectoryMatch <http://httpd.apache.org/docs/2.2/mod/core.html#directorymatch>`_
* `Files> <http://httpd.apache.org/docs/2.2/mod/core.html#files>`_
* `FilesMatch <http://httpd.apache.org/docs/2.2/mod/core.html#filesmatch>`_
* `Location <http://httpd.apache.org/docs/2.2/mod/core.html#location>`_
* `LocationMatch <http://httpd.apache.org/docs/2.2/mod/core.html#locationmatch>`_
* `VirtualHost <http://httpd.apache.org/docs/2.2/mod/core.html#virtualhost>`_
Localiza algunas de ellas en los ficheros de configuración.

6. ¿Qué son los ficheros .htaccess?
