Ejercicio: Instalación y configuración básica de Apache
=======================================================

Instalación de Apache 2.4
-------------------------

1. Instala el servidor web Apache e indica el FQDN para que al inciar el servicio no nos de ningún problema.

Para controlar el servicio apache2 podemos usar: (para más información <http://httpd.apache.org/docs/2.4/es/stopping.html>)::

    apache2ctl [-k start|restart|graceful|graceful-stop|stop]

2. ¿Qué es la opción graceful?

3. Comprueba la directiva donde indicamos el puerto de escucha del servidor. Modifica el puerto de escucha para que sea el 8080. Comprueba el acceso al servidor desde un navegador.

4. Comprueba los módulos  cargados en el servidor.

5. Comprueba los sitios webs activos en nuestro servidor.

Estructura de los ficheros de configuración
-------------------------------------------

1. Las directivas de configuración de apache2 se pueden aplicar si está definido un determinado parámetro. Para esto se utiliza la directiva * `IfDefine <http://httpd.apache.org/docs/2.4/mod/core.html#ifdefine>`_. Busca en algún fichero de configuración esta directiva.

2. Igualmente podemos aplicar determinadas directivas si hay cargado un determinado módulo, para ello usamos `IfModule <http://httpd.apache.org/docs/2.4/mod/core.html#ifmodule>`_. Busca alguna directiva de este tipo.

    Para cargar dinámicamente los módulos se utilza la directiva `LoadModule <http://httpd.apache.org/docs/2.4/mod/mod_so.html#loadmodule>`_, búscalos en los ficheros .load dentro de ``/etc/apache2/mods-availables``.

    Más información: http://httpd.apache.org/docs/2.4/dso.html

3. Busca en la configuración una variable de entorno y determina en que fichero están definidas.

4. La directiva `Include <http://httpd.apache.org/docs/2.4/mod/core.html#include>`_
 nos permite añadir ficheros de configuración a la configuración general de apache2. Comprueba qué ficheros son añadidos con esta directiva.

5. Podemos aplicar directivas a partes concretas de nuestro servidor web, para ello estudia las siguientes directivas (Para aprender más lee `Secciones de Configuración <http://httpd.apache.org/docs/2.4/sections.html>`_):

* `Directory <http://httpd.apache.org/docs/2.4/mod/core.html#directory>`_
* `DirectoryMatch <http://httpd.apache.org/docs/2.4/mod/core.html#directorymatch>`_
* `Files <http://httpd.apache.org/docs/2.4/mod/core.html#files>`_
* `FilesMatch <http://httpd.apache.org/docs/2.4/mod/core.html#filesmatch>`_
* `Location <http://httpd.apache.org/docs/2.4/mod/core.html#location>`_
* `LocationMatch <http://httpd.apache.org/docs/2.4/mod/core.html#locationmatch>`_
* `VirtualHost <http://httpd.apache.org/docs/2.4/mod/core.html#virtualhost>`_
Localiza algunas de ellas en los ficheros de configuración.

6. ¿Qué son los ficheros .htaccess?

Configuración básica de Apache
------------------------------

Busca en el fichero de configuración de Apache las siguientes directivas, determina que función tienen y el valor que poseen por defecto.

Directivas de identificación del servidor:

* `ServerName <http://httpd.apache.org/docs/2.4/mod/core.html#servername>`_
* `ServerAdmin <http://httpd.apache.org/docs/2.4/mod/core.html#serveradmin>`_
* `ServerTokens <http://httpd.apache.org/docs/2.4/mod/core.html#usecanonicalname>`_

Modifica el valor de ServerAdmin y ServerTokens y comprueba los resultados.

Directivas de localización de ficheros

* `DocumentRoot <http://httpd.apache.org/docs/2.4/mod/core.html#documentroot>`_
* `ErrorLog <http://httpd.apache.org/docs/2.4/mod/core.html#errorlog>`_
* `CustomLog <http://httpd.apache.org/docs/2.4/mod/mod_log_config.html#customlog>`_
* `LockFile <http://httpd.apache.org/docs/2.4/mod/mpm_common.html#lockfile>`_
* `PidFile <http://httpd.apache.org/docs/2.4/mod/mpm_common.html#pidfile>`_
* `ServerRoot <http://httpd.apache.org/docs/2.4/mod/core.html#serverroot>`_
* `AccessFileName <http://httpd.apache.org/docs/2.0/mod/core.html#accessfilename>`_

Directivas de control de la conexión

* `Timeout <http://httpd.apache.org/docs/2.4/mod/core.html#timeout>`_
* `KeepAlive <http://httpd.apache.org/docs/2.4/mod/core.html#keepalive>`_`Más información <http://systemadmin.es/2011/08/conexiones-con-keepalive-en-http1-0>`_
* `MaxKeepAliveRequests <http://httpd.apache.org/docs/2.4/mod/core.html#maxkeepaliverequests>`_
* `KeepAliveTimeout <http://httpd.apache.org/docs/2.4/mod/core.html#keepalivetimeout>`_

Otras directivas

* `User <http://httpd.apache.org/docs/2.0/mod/mpm_common.html#user>`_
* `Group <http://httpd.apache.org/docs/2.0/mod/mpm_common.html#group>`_
* `DefaultType <http://httpd.apache.org/docs/2.0/mod/core.html#defaulttype>`_
* `LogLevel <http://httpd.apache.org/docs/2.0/mod/core.html#loglevel>`_
* `LogFormat <http://httpd.apache.org/docs/2.0/mod/mod_log_config.html#logformat>`_
