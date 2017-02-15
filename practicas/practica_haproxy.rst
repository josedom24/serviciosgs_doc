Práctica: Balanceo de carga en servidores Apache con HAproxy
============================================================


.. note::

	**(9 tareas - 20 puntos)(4 tareas obligatorias - 9 puntos)**

.. note::

	* Muestra al profesor: Tareas 1,2,3,4,5,6 
    
En primer lugar, construye con KVM con vagrant la siguiente infraestructura:

.. image:: img/haproxy.jpg

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

En apache2::

    apache2:~# nano /var/www/html/index.html
    ...
     <h1> Servidor por APACHE_DOS </h1>
     ...

3. Crear en ambas máquinas (apache1, apache2) el script PHP sleep.php::

    apache1~:# nano /var/www/html/sleep.php 

     <html>
         <title> Retardos de x segundos </title>
     <body>
         <h1> Prueba con retardo de x segundos </h1>
         <p> hora de inicio: <?php echo date('h:i:s'); ?> </p>
         <?php
         for ($i=0; $i < 2000000; $i++) { 
             $str1 = sha1(rand()*rand());
             $str2 = sha1(rand()*rand());
             $str3 = sha1($str1+$str2);
         }
         ?>
         <p> hora de fin: <?php echo date('h:i:s'); ?> </p>
     </body>
     </html>

Comprobación::

    apache1~:# php /var/www/html/sleep.php
    apache2~:# php /var/www/html/sleep.php

Evaluar rendimiento de un servidor Apache sin balanceo
------------------------------------------------------

Se realizarán varias pruebas de carga sobre el servidor Apache ubicado en la máquina apache1. Pasos a realizar:

1. Habilitar en *balanceador* la redirección de puertos para que sea accesible el servidor Apache de la máquina apache1 [10.10.10.11] empleando el siguiente comando iptables::

    balanceador:~# echo 1 > /proc/sys/net/ipv4/ip_forward
    balanceador:~# iptables -t nat -A PREROUTING \
                             --in-interface eth0 --protocol tcp --dport 80 \
                             -j DNAT --to-destination 10.10.10.11

.. warning::

    Nota: la regla iptables establece una redirección del puerto 80 de la máquina balanceador al mismo puerto de la máquina apache1 para el tráfico procedente de la red externa (interfaz de entrada eth0).

2. Arrancar en apache1 [10.10.10.11] el servidor web Apache2:

    apache1:~# systemctl start apache2

.. warning::

    Nota: Desde la máquina cliente se puede abrir en un navegador web la URL http://172.22.x.x para comprobar que el servidor está arrancado y que la redirección del puerto 80 está funcionando.



3. Lanzar las pruebas de carga iniciales sobre balanceador usando el herramienta Apache Benchmark

*Prueba 1: Contenido estático*::

    cliente:~# ab -n 2000 -c 10 http://172.22.x.x/index.html
    cliente:~# ab -n 2000 -c 50 http://172.22.x.x/index.html
    cliente:~# ab -n 2000 -c 100 http://172.22.x.x/index.html

Envía 2000 peticiones HTTP sobre la URI "estática", manteniendo, respectivamente, 10 y 50 conexiones concurrentes.

*Prueba 2: Scripts PHP*

Se usará un script PHP (sleep.php) que introduce un retardo mediante un bucle “activo” de 2000000 iteraciones que busca forzar el uso de CPU con cálculos de hashes SHA1 y concatenaciones de cadenas::

    cliente:~# ab -n 250 -c 10 http://172.22.x.x/sleep.php
    cliente:~# ab -n 250 -c 30 http://172.22.x.x/sleep.php
    cliente:~# ab -n 250 -c 50 http://172.22.x.x/sleep.php

Envía 250 peticiones HTTP sobre la URI “dinámica”, manteniendo, respectivamente, 10 y 30 conexiones concurrentes. (aprox 5-7 minutos)
