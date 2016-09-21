¿Cómo funciona el servidor DHCP
===============================

El protocolo de configuración dinámica de host (Dynamic Host Configuration Protocol – DHCP)  es una extensión de protocolo BOOTP que da más flexibilidad al administrar las direcciones IP.  Este protocolo puede usarse para configurar dinámicamente los parámetros esenciales TCP/IP de los hosts (estaciones de trabajo y servidores)  de una red.  El protocolo DHCP tiene dos elementos:

* Un mecanismo para asignar direcciones IP y otros parámetros TCP/IP. 
* Un protocolo para negociar y transmitir información específica del host. 

El host TCP/IP que solicita la información de configuración TCP/IP se denomina cliente DHCP y el host que provee dicha información se llama servidor DHCP. El DHCP se describe en la norma **RFC 2131** –Protocolo de configuración dinámica de host–.  A continuación, presentamos la operación del DHCP. 

Administración de direcciones con el DHCP
-----------------------------------------

El protocolo DHCP usa los siguientes 3 métodos para asignar las direcciones IP:

**a) Asignación manual**
	El administrador de red pone manualmente la dirección IP del cliente DHCP en el servidor DHCP. El DHCP se usa para dar al cliente DHCP el valor de esta dirección IP configurada manualmente. 
**b) Asignación automática**
	No se requiere asignar manualmente direcciones IP.  El servidor DHCP asigna al cliente DHCP, en el primer contacto, una dirección IP permanente que no podrá reutilizar ningún otro cliente DHCP. 
**c) Asignación dinámica**
	El DHCP asigna una dirección IP al cliente DHCP por un tiempo determinado.  Después que expire este lapso, se revoca la dirección IP y el cliente DHCP tiene que devolverla.  Si el cliente aún necesita una dirección IP para efectuar sus operaciones, deberá solicitarla nuevamente. 

Este protocolo permite la reutilización automática de una dirección IP.  Si un cliente DHCP ya no necesita una dirección IP, como en el caso de un ordenador que apagamos, éste libera
su dirección y la entrega al servidor DHCP.  Éste puede reasignar dicha dirección a otro cliente que la pida. 

El método de asignación dinámica es muy útil para clientes DHCP que necesitan una dirección IP para una conexión temporal a la red.  Por ejemplo, consideremos una situación en que 300 usuarios tengan ordenadores portátiles conectadas a una red y ésta les ha asignado direcciones clase C.  Este tipo de dirección permite a la red tener hasta 253 nodos (255 – 2 direcciones especiales = 253). Debido a que los ordenadores que se conectan a una red usando el TCP/IP requieren tener una dirección única IP, entonces las 300 ordenadores no podrían operar simultáneamente.  Sin embargo, si sólo hay 200 conexiones físicas a la red se puede buscar una dirección de clase C mediante la reutilización de direcciones IP no usadas.  Usando el DHCP, en su método de asignación dinámica de direcciones IP, es posible reutilizar direcciones IP. 

Además la asignación dinámica de direcciones IP es un buen método para asignar direcciones IP a ordenadores que van a ser conectados por primera vez y en una red donde escasean las direcciones IP.  Si los ordenadores antiguos se retiran, sus direcciones IP pueden ser reutilizadas o reasignadas inmediatamente. Sin importar cuál método se elija, aún puede configurarse los parámetros IP de una sola vez desde un servidor central, en lugar de repetir la configuración TCP/IP para cada ordenador.

