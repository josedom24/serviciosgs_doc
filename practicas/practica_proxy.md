# Práctica: Servidor proxy/cache squid

```eval_rst
.. note::

	**(8 tareas - 20 puntos)(4 tareas obligatorias - 7 puntos)**

.. note::

	* Muestra al profesor: Tareas 1,2,3,4,5,6 
```

En primer lugar, construye con KVM con vagrant la siguiente infraestructura:

.. image:: img/esquema.png

## Proxy squid

Queremos instalar un servidor proxy/cache en nuestro **servidor 1**. Con ello vamos a poder controlar las páginas web a las que accedamos (desde el **servidor 2** y **servidor 3**), además de acelerar nuestra navegación.

Nos piden la configuración de un proxy/cache/filtro en nuestra infraestrucutra. Hemos elegido como proxy/cache squid3, y como filtro de contenido dansguardian. Tenemos que tener en cuenta las siguientes consideraciones:

1. El proxy/cache sólo admite conexiones de la red local.
2. Se quieren limitar las siguientes conexiones:
    * No se pueden bajar ficheros que se puedan instalar (``exe,msi,rar,zip,bin,iso``).
    * No tienen acceso a internet los fines de semana.
3. El control de las páginas permitidas se hará mediante listas negras usando dansguardians.
4. Por último tendremos instalado un programa para monitorizar el uso del proxy: sarg. Para visualizar la información generada por dicho programa accederemos a una página web llamada ``proxy.josedomingo.gonzalonazareno.org`` que sólo será accesible si ponemos el nombre de usuario y contraseña.
5. Finalmente queremos configurar la infraestrucutra para tener un proxy transparente.

```eval_rst
.. note::

    * **Tarea 1 (1 punto)(Obligatorio)**: Configura de forma manual el proxy. Muestra las capturas de pantalla.
    * **Tarea 2 (2 puntos)(Obligatorio)**: Muestra la configuración de squid para no permitir descargar ficheros ejecutables. Prueba de funcionamiento.
    * **Tarea 3 (2 puntos)(Obligatorio)**: Muestra la configuración de squid para no permitir el acceso los fines de semana. Prueba de funcionamiento.
    * **Tarea 4 (2 puntos)**: Filtra el dominio youtube.com en la lista negra y prueba que realmente no se puede acceder.
    * **Tarea 5 (2 puntos)**: Documenta la instalación de sarg, y muestra las estadísticas de accceso al proxy con sarg.
    * **Tarea 6 (3 puntos)**: Documenta la configuración del proxy transparente y haz una prueba de funcionamiento.
```

## Proxy inverso

```eval_rst
.. note::

    Seguimos trabajando con las mismas máuinas, pero en un ejercicio nuevo, por lo que si necesitas detener los servicios del ejercicio anterior lo puedes hacer.
```

En este caso queremos instalar dos servidor web en el **Servidor 2** y en **Servidor 3**, estos servidores simplemente deben ofrecer una página de bienvenida donde se vea el nombre del servidor ("Bienvenido al Servidor 2").

En el servidor 1 vamos a instalar diferentes configuraciones de proxy inverso para que desde el exterior se puedan acceder a las páginas de los servidores conectados a la red interna.




