# Práctica: Ejecución de script PHP. Rendimiento.

.. note::

    (9 tareas - 30 puntos)(6 tareas obligatorias - 12 puntos)
    
    
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

	    * **Tarea 1 (2 punto)(Obligatorio)**: Documenta la instalación del módulo php de apache2. Muestra wordpress funcionando con el módulo php de apache2. Realiza una comprobación de que, efectivamente, se está usando el módulo php.
	    * **Tarea 2 (2 puntos)(Obligatorio)**: Documenta la instalación y configuración de memcached. Entrega una comprobación de que memcached está funcionando.
	    * **Tarea 3 (2 puntos)(Obligatorio)**: Documenta la instalación y configuración de varnish. Entrega una comprobación de que varnish está funcionando.
	    * **Tarea 4 (2 puntos)(Obligatorio)**: Documenta la instalación y configuración de FPM-PHP con el módulo de multiprocesamiento event (desinstala el memcached y vanish). Muestra wordpress funcionando con FPM-PHP. Realiza una comprobación de que, efectivamente, se está usando FPM-PHP.
	    * **Tarea 5 (2 puntos)(Obligatorio)**: Entrega y muestra una comprobación de que memcached está funcionando con la nueva configuración.
	    * **Tarea 6 (2 puntos)(Obligatorio)**: Entrega y muestra una comprobación de que varnish está funcionando con la nueva configuración.

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
