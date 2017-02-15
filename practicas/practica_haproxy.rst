Práctica: Balanceo de carga en servidores Apache con HAproxy
============================================================


.. note::

	**(9 tareas - 20 puntos)(4 tareas obligatorias - 9 puntos)**

.. note::

	* Muestra al profesor: Tareas 1,2,3,4,5,6 
    
En primer lugar, construye con KVM con vagrant la siguiente infraestructura:

.. img:: img/haproxy.jpg

Ajustar la configuración de las dos máquinas del cluster de balanceo (apache1 y apache2):

1. Deshabilitar la opción KeepAlive en el fichero de configuración ``/etc/apache2/apache2.conf`` para realizar la evaluación del rendimiento sin la opción de reutilización de conexiones::

    apache1:~# nano /etc/apache2/apache2.conf
     ...
     KeepAlive Off
     ...            

     apache2:~# nano /etc/apache2/apache2.conf
     ...
     KeepAlive Off
     ...

.. warning:: 

    Nota: este ajuste no es estrictamente necesario (y sería desaconsejable en un entorno de producción real), pero facilita las pruebas manuales dado que permite detectar inmediatamente el “cambio” de destino resultado del balanceo de carga manteniendo la opción por defecto, en las pruebas manuales desde el navegador sería necesario esperar 5 segundos (el time out de keep alive) antes de recargar la página y ver el efecto del reparto de carga

2. Editar los archivos del sitio web para incluir una indicación del servidor real que está sirviendo una petición, de modo que sea posible "diferenciarlos" en las pruebas manuales con el navegador

En apache1::

    apache1:~# nano /var/www/html/index.html
     ...
     <h1> Servidor por APACHE_UNO </h1>
     ...
     apache1:~# nano /var/www/html/sesion.php   
            

     <?php
     header('Content-Type: text/plain');
     session_start();
     if(!isset($_SESSION['visit']))
     {
             echo "This is the first time you're visiting this server";
             $_SESSION['visit'] = 0;
     }
     else
             echo "Your number of visits: ".$_SESSION['visit'];         

     $_SESSION['visit']++;          

     echo "\nServer IP: ".$_SERVER['SERVER_ADDR'];
     echo "\nClient IP: ".$_SERVER['REMOTE_ADDR'];
     echo "\nX-Forwarded-for: ".$_SERVER['HTTP_X_FORWARDED_FOR']."\n";
     print_r($_COOKIE);
     ?>

En apache2:

    apache2:~# nano /var/www/html/index.html
    ...
     <h1> Servidor por APACHE_DOS </h1>
     ...

        