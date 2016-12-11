Ejercicio: Módulos de Multiprocesamiento (MPMs)
===============================================

Por defecto apache2 se configura con el MPM event, podemos ver el MPM que estamos utilizando con la siguiente instrucción::

	# apachectl -V
	...
	Server MPM:     event
	...

Para cambiar de MPM tenemos que desactivar el actual y activar el nuevo módulo::

	# a2dismod mpm_event
	# a2enmod mpm_prefork
	# service apache2 restart

	# apachectl -V
	...
	Server MPM:     prefork
	...

**Las directivas de configuración de los distintos MPM**

En ``/etc/apache2/mods-availables/mpm_prefork.conf``::

Directivas de control de `prefork <http://httpd.apache.org/docs/2.4/mod/prefork.html>`_

    StartServers          5
    MinSpareServers       5
    MaxSpareServers      10
    MaxClients          150
    MaxRequestsPerChild   0

En ``/etc/apache2/mods-availables/mpm_worker.conf``::

Directivas de control de `worker <http://httpd.apache.org/docs/2.4/mod/worker.html>`_

    StartServers          2
    MinSpareThreads      25
    MaxSpareThreads      75
    ThreadLimit          64
    ThreadsPerChild      25
    MaxClients          150
    MaxRequestsPerChild   0

En ``/etc/apache2/mods-availables/mpm_event.conf``::

Directivas de control de `event <http://httpd.apache.org/docs/2.4/mod/event.html>`_

    StartServers              2
    MinSpareThreads          25
    MaxSpareThreads          75
    ThreadLimit              64
    ThreadsPerChild          25
    MaxRequestWorkers       150
    MaxConnectionsPerChild    0



