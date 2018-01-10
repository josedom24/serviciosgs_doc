# Práctica: Configuración de un servidor Windows Server 2012

```eval_rst
.. note::

	(8 tareas - 20 puntos)
```

## Esquema de red

Debes configurar en un entorno virtual en KVM donde tengas 3 máquinas:

* Un servidor Windows Server 2012 con dos interfaces de red, uno conectado a internet, y otro a una red intena donde se encuentran los clientes.
* Dos clientes: uno Linux y otro Windows.

```eval_rst
.. warning::

	* **Tarea 1 (2 puntos):**  Configuración de la red virtual en KVM. Indica el nombre que le has puesto al ordenador servidor. Y por último, indica la configuración de red del servidor y de algún cliente.
	* **Tarea 2 (2 puntos):**  Explica la configuración del servidor para que funcione como router y nat.
```

## Servidor DHCP


Los ordenadores clientes de nuestra LAN obtienen su configuración de red ofrecidas por dicho servidor, que tiene las siguientes características:

	* Rango: 192.168.1.3-192.168.1.254
	* Máscara de red: 255.255.255.0 
	* Puerta de enlace: La ip del router
	* DNS: Según el que te convenga para hacer las pruebas 

Crea una reserva para el que uno de los clientes tome siempre una dirección fija.

```eval_rst
.. warning::

	* **Tarea 3 (3 puntos):**  Muestra al profesor el servidor DHCP funcionando. Muestra el fichero de configuración del servidor, la lista de concesiones, la modificación en la configuración que has hecho en el cliente para que tome la configuración de forma automática y muestra la salida del comando ifconfig.
	* **Tarea 4 (2 puntos):** Indica las modificaciones realizadas en el servidor y muestra al profesor una comprobación de que el cliente ha tomado esa dirección.
```

## Servidor DNS

Lo primero que tienes que hacer es determinar un nombre de dominio que va a ser utilizado en nuestro sistema. (En esta documentación voy a utilizar el nombre ``example.com``). El servidor DNS ofrece el servicio de resolución de nombres para los ordenadores de nuestra red local. Debes tener en cunta los siguientes puntos:

	* Cuando tengas funcionando el servidor DNS, tendrás que modificar el servidor DHCP para que los clientes usen el nuevo servidor DNS. 
	* Piensa el nombre que tiene el servidor. El servidor DNS debe poder resolver los siguientes nombres: ``nombredelservidor.example.com``, ``www.example.com``, ``informatica.example.com``. El primero es el nombre del servidor, los dos siguientes son dos páginas webs que el servidor va a servir. 
	* Debes implementar la zona inversa del servidor.

```eval_rst
.. warning::

	* **Tarea 5 (3 puntos):** Realiza la instalación y configuración del servidor DNS con las características anteriomente señaladas. Indica el cambio que hay que hacer en el servidor dhcp para que el sistema funcione de manera adecuada. Entrega una captura de pantalla donde se vea las zonas que has definido. Muestra el resultado al profesor.
	* **Tarea 6 (3 puntos):** Realiza las consultas dig/nslookup desde los clientes preguntando por los siguientes:
	* Dirección de ``www.example.com``
	* El servidor DNS con autoridad sobre la zona del dominio 
	* La dirección IP de ``www.josedomingo.org``
	* Una resolución inversa
```

## Servidor WEB

El servidor tiene instalado un servidor Web IIS, que sirve dos virtual host con páginas web estáticas.

* ``www.example.com``: Página principal del centro.
* ``informatica.example.com``: Página del departamento de informática
* La página ``www.example.com``, posee un directorio /privado, que para acceder a el es necesario autentificarse.

```eval_rst
.. warning::

	* **Tarea 7 (3 puntos):** Configura el servidor web para servir las dos páginas. Busca plantillas html+css como contenido para las dos páginas, modificandolas un poco para que parezcan más reales. Muestra las páginas al profesor.
	* **Tarea 8 (2 puntos):** Autentificación de la carpeta /privado: Sólo se pueden autentificar los usuarios del sistemas que pertenezcan al grupo profesores. Muestra el funcionamiento al profesor.
```