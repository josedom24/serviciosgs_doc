# Aumento de rendimiento en servidores web



**Aceleradores PHP**

El objetivo principal de un acelerador PHP es guardar los scripts php ya compilando, obteniendo un mayor rendimiento en la respuesta del servidor. El acelerador se puede usar usando el módulo php de apache o usando fastcgi. Más información sobre [aceleradores PHP+(http://www.maestrosdelweb.com/aceleradores-de-php/>).

Desde la versión 5.5 de php ya tenemos una cache de código instalada como módulo. En la documentación de PHP 5.5 podemos leer: *“La caché de códigos de operación de Zend Optimiser+ se ha añadido a PHP como la nueva extensión OPcache. OPcache mejora el rendimiento de PHP almacenando código de byte de un script precompilado en la memoria compartida, eliminando así la necesidad por parte de PHP de cargar y analizar scripts en cada petición.”*

Podemos obtener información acerca de como configurar `opcache` en la página: [How To: Enable PHP 7 OPcache on Ubuntu 16.04](https://lastplaceonthe.net/how-to-enable-php-7-opcache-on-ubuntu-16-04/).

**Memcached**

[Memcached+(http://memcached.org/>) es un sistema distribuido de propósito general y que es muy usado en la actualidad por múltiples sitios web. Memcached es empleado para el almacenamiento en caché de datos u objetos en la memoria RAM, reduciendo así las necesidades de acceso a un origen de datos externo (como una base de datos o una API).

* [Manual de instalación de memcached+(http://www.pontikis.net/blog/install-memcached-php-debian>)
* [Como utilizar Memcached con WordPress+(https://raiolanetworks.es/blog/como-utilizar-memcached-con-wordpress/>)
* [Memcached para optimizar WordPress](https://raiolanetworks.es/blog/memcached/#memcached_para_optimizar_wordpress)

**Varnish**

Varnish es un acelerador HTTP que funciona como un proxy inverso. Se sitúa por delante del servidor web, cacheando la respuesta de dicho servidor web en memoria. La próxima vez que un visitante visite la misma URL, la página será servida desde Varnish en lugar de desde el servidor web, ahorrando recursos en el backend y permitiendo más conexiones simultáneas.

* [Presentación Madrid DevOps (Varnish: funcionamiento, configuración y uso)+(http://www.youtube.com/watch?v=A5poVWqjJrs>)
* [http://pabloroman.es/blog/2013/01/20/como-usar-varnish-para-acelerar-tu-sitio-web/+(http://pabloroman.es/blog/2013/01/20/como-usar-varnish-para-acelerar-tu-sitio-web/>)
* [How to: Varnish listen port 80 with systemd+(http://deshack.net/how-to-varnish-listen-port-80-systemd/>)
* [http://pabloroman.es/blog/2013/05/20/varnish-3-trucos-y-consejos/+(http://pabloroman.es/blog/2013/05/20/varnish-3-trucos-y-consejos/>)
* [https://scalr-wiki.atlassian.net/wiki/display/docs/Install+Varnish+HTTP+Accelerator+with+WordPress+(https://scalr-wiki.atlassian.net/wiki/display/docs/Install+Varnish+HTTP+Accelerator+with+WordPress>)
* [http://kontsu.wordpress.com/2012/10/10/apache-2-performance-boost-with-varnish-yslow/+(http://kontsu.wordpress.com/2012/10/10/apache-2-performance-boost-with-varnish-yslow/>)
 * [Put Varnish on port 80+](http://www.varnish-cache.org/docs/trunk/tutorial/putting_varnish_on_port_80.html>)

