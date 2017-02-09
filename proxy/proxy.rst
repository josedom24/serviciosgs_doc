Gestionando el proxy de squid
=============================

En este apartado vamos a ver como controlar el proxy por medio de ACL.

Para crear controles de acceso basados en el **origen** de la petición del cliente podemos usar los siguientes tipos de elementos de ACL:

* src: Dirección IP del cliente, puede ser una sola dirección lista o rango de direcciones IP, soporta el uso de mascaras de subred en formato CIDR
* proxy_auth: Autenticación de usuarios vía procesos externos
* browser: User-agent del navegador web que realiza la petición

Para crear controles de acceso basados en el **destino** de la petición encontramos los siguientes tipos de elementos de ACL:

* dstdomain: Este tipo define uno o más dominios destino solicitados por el cliente
* url_regex: Tipo con soporte de expresiones regulares para el URL solicitado por el cliente
* urlpath_regex: URL-path regular expression pattern matching, leaves out the protocol and hostname
* port: Este tipo define uno o más números de puerto destino solicitados por el cliente
* method: Este tipo define el método usado por el cliente para la petición HTTP (get, post, etc)

Para crear controles de acceso basados en el **tipo MIME** de la solicitud o respuesta de la petición podemos usar los siguientes tipos de elementos de ACL:

* req_mime_type: regular expression pattern matching on the request content-type header
* rep_mime_type: regular expression pattern matching on the reply (downloaded content) content-type header.

Además es posible crear controles de acceso basados en el **tiempo** en el que se realiza la petición, y usando procesos externos, por ejemplo para realizar autenticación basada en grupos, las ACLs que podemos usar son:

* time: hora del día, y día de la semana

Reglas de control de acceso
---------------------------

Los controles de acceso se realizan principalmente con la directiva http_access para peticiones HTTP y http_reply_access para las respuestas HTTP.

Las reglas http_access se usan para permitir o denegar el acceso a uno o más elementos de ACL, es decir, se podría evaluar tanto el origen: dirección IP, usuario, o el destino: dominio o URL de la petición, por mencionar algunos tipos. Squid tomará toda la información posible de las cabeceras de la petición HTTP.

El esquema más simple las reglas http_access para determinar el acceso a un a un elemento sería el siguiente::

	http_access allow|deny acl

Squid evalúa las reglas en el orden en el que son escritas, es decir, de arriba hacía abajo. Si la primer regla no hace coincidencia con la petición, entonces el squid realizará una operación de tipo OR y evaluará los elementos de la siguiente regla de acceso::

	http_access allow|deny acl
	                OR
	http_access allow|deny acl
	                OR
	...

Si en una regla de acceso hay más de un elemento de ACL, el sistema utiliza el operador AND para cada elemento de la regla, esto quiere decir, que todos los elementos de la ACL deben hacer coincidencia para que una acción se aplique::

	http_access allow|deny acl AND acl AND ...
	                OR
	http_access allow|deny acl AND acl AND ...
	                OR
	...
	http_access deny all

Para más información sobre la creación de ACL puedes mirar los siguientes enlaces:

* `Introducción a los esquemas de control de acceso en Squid  <http://web.archive.org/web/20151027022458/http://tuxjm.net/docs/Manual_de_Instalacion_de_Servidor_Proxy_Web_con_Ubuntu_Server_y_Squid/html-multiples/configuracion-de-los-esquemas-de-control-de-acceso-en-squid.html>`_
* `Manual de Instalación de Servidor Proxy Web con Squid <https://github.com/josedom24/serviciosgs_doc/raw/master/proxy/doc/Squid_v4_mas_Webmin.pdf>`_

Autenticación por usuarios y grupos con Squid
---------------------------------------------

En esta sección se describen los procedimientos para configurar el proxy Squid para autenticar usuarios usando diferentes métidos de autenticación.

Módulos de autenticación de usuarios Squid

* NCSA 	Usa un archivo de usuarios y contraseñas al estilo NCSA
* LDAP 	Usa el protocolo Lightweight Directory Access Protocol
* MSNT 	Usa un dominio de autenticación Windows NT
* PAM 	Usa los módulos de autenticación PAM
* SMB 	Usa un servidor SMB como Windows NT o Samba

Para autentificar usuarios hay que usar ACL de tipo ``proxy_auth``.

Para más información:

* * `Introducción a los esquemas de control de acceso en Squid  <http://web.archive.org/web/20151027022458/http://tuxjm.net/docs/Manual_de_Instalacion_de_Servidor_Proxy_Web_con_Ubuntu_Server_y_Squid/html-multiples/configuracion-de-los-esquemas-de-control-de-acceso-en-squid.html>`_

