# Práctica: Ejecución de script PHP. Rendimiento.

.. note::

    (9 tareas - 30 puntos)(9 tareas obligatorias - 11 puntos)
    
    
Vamos a comparar el rendimiento de distintas configuraciones de servidores web sirviendo páginas dinámicas programadas con PHP, en concreto vamos a servir una CMS Wordpress.

Las configuraciones que vamos a realizar son las siguientes:
	
	* Módulo php5-apache2
	* FPM-PHP + apache2
	* FPM-PHP + apache2 + memcached
	* FPM-PHP + apache2 + varnish
	* FPM-PHP + nginx 
	* FPM-PHP + nginx + memcached
	* FPM-PHP + nginx + varnish

.. note::

		* Apache2

	    * **Tarea 1 (1 punto)(Obligatorio)**: Documenta la instalación del módulo php de apache2. Muestra wordpress funcionando con el módulo php de apache2. Realiza una comprobación de que, efectivamente, se está usando el módulo php.
	    * **Tarea 2 (1 punto)(Obligatorio)**: Documenta la instalación y configuración de FPM-PHP y apache2 (escuchando en un socket UNIX) con el módulo de multiprocesamiento event. Muestra wordpress funcionando con FPM-PHP. Realiza una comprobación de que, efectivamente, se está usando FPM-PHP.
	    * **Tarea 3 (1 punto)(Obligatorio)**: Cambia la configuración anterior para que FPM-PHP escuche en un socket TCP.
	    * **Tarea 4 (1 punto)(Obligatorio)**: Añade a la configuración anterior memcached. Documenta la instalación y configuración memcached. Recuerda que para que Wordpress utilice memcached le tenemos que instalar un plugin. Muestra las estadísticas de memcached después de acceder varias veces a wordpress para comprobar que esa funcionando.
	    * **Tarea 5 (2 puntos)(Obligatorio)**: Configura un proxy inverso - caché Varnish escuchando en el puerto 80 y que se comunica con el servidor web por el puerto 8080. Entrega y muestra una comprobación de que varnish está funcionando con la nueva configuración.

	    * nginx

	    * **Tarea 6 (1 punto)(Obligatorio)**: Documenta la instalación y configuración de FPM-PHP y nginx (escuchando en un socket UNIX) con el módulo de multiprocesamiento event. Muestra wordpress funcionando con FPM-PHP. Realiza una comprobación de que, efectivamente, se está usando FPM-PHP.
	    * **Tarea 7 (1 punto)(Obligatorio)**: Cambia la configuración anterior para que FPM-PHP escuche en un socket TCP.
	    * **Tarea 8 (1 punto)(Obligatorio)**: Añade a la configuración anterior memcached. Documenta la instalación y configuración memcached. Recuerda que para que Wordpress utilice memcached le tenemos que instalar un plugin. Muestra las estadísticas de memcached después de acceder varias veces a wordpress para comprobar que esa funcionando.
	    * **Tarea 9 (2 puntos)(Obligatorio)**: Configura un proxy inverso - caché Varnish escuchando en el puerto 80 y que se comunica con el servidor web por el puerto 8080. Entrega y muestra una comprobación de que varnish está funcionando con la nueva configuración.
	    


	Ahora puedes realizar el trabajo y generar la documentación en pdf requerida, teniendo en cuenta los siguientes puntos:

	    * **Tarea 7 (4 puntos)**: Introducción del trabajo. Explica los objetivos de la práctica. Explica los módulos de multiprocesamiento.
	    * **Tarea 8 (6 puntos)**: Generación de las gráficas.
	    * **Tarea 9 (8 puntos)**: Conclusiones. Explica razonadamente a las conclusiones que has llegado.


Genera una documentación que al menos tenga los siguientes puntos:

	1. Introducción. Explicación de los módulos de multiprocesamiento. Objetivos de la práctica.
	2. Configuración de los escenarios:
		* Instalación del módulo php de apache2.
		* Instalación y configuración de memcached
		* Instalación y configuración de vanish
		* Instalación y configuración de FPM-PHP con el módulo de multiprocesamiento event
		* Configuración de memcached y vanish con la nueva configuración
	3. Generación de las grafícas de uso de memoria: una para cada configuración en cada una de las cargas (18 en total).
	4. Generación de las gráficas de rendimiento: una para cada carga, con 6 gráficas.
	5. CONCLUSIONES. Lo más valorado en la tarea serán las conclusiones a las que llegas.
