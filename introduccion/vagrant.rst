Introducción a vagrant
======================

Vagrant es una aplicación libre desarrollada en ruby que nos permite crear y personalizar entornos de desarrollo livianos, reproducibles y portables. Vagrant nos permite automatizar la creación y gestión de máquinas virtuales. Las máquinas virtuales creadas por vagrant se pueden ejecutar con distintos gestores de máquinas virtuales (oficialmente VirtualBox, VMWare e Hyper-V), en nuestro ejemplo vamos a usar máquinas virtuales en VirtualBox.

El objetivo principal de vagrant es aproximar los entornos de desarrollo y producción, de esta manera el desarrollador tiene a su disposición una manera  muy sencilla de desplegar una infraestructura similar a la que se va a tener en entornos de producción. A los administradores de sistemas les facilita la creación de infraestructuras de prueba y desarrollo.

`Presentación: Vagrant y ansible. Una combinación explosiva (1ª parte) <http://iesgn.github.io/cloud/curso/u2/presentacion_vagrant>`_

Prácica con vagrant
-------------------

* **Práctica 1: Instalación de vagrant**

Instalar virtualbox y vagrant::

    root@maquina:~$ apt-get install virtualbox
    root@maquina:~$ wget https://releases.hashicorp.com/vagrant/1.8.5/vagrant_1.8.5_x86_64.deb
    root@maquina:~$ dpkg -i vagrant_1.8.5_x86_64.deb

* **Práctica 2: Instalación de un "box" debian/jessie**

Nos descargamos desde el repositorio oficial el box de Debian Jessie de 64 bits, esto lo hacemos un usuario sin privilegios:::

    usuario@maquina:~$ vagrant box add debian/jessie64

Si el box lo tenemos en la *nas* de nuestro instituto:::

    usuario@maquina:~$ vagrant box add debian/jessie64 http://nas.gonzalonazareno.org/...

.. note:: Es importante fijarnos que lo estamos haciendo con usuarios sin privilegios. Cada usuario tendrás sus box propios.
        
Puedo ver la lista de boxes que tengo instalada en mi usuario ejecutando la siguiente instrucción:::

    usuario@maquina:~$ vagrant box list

* **Práctica 3: Creación de una máquina virtual**

1. Nos creamos un directorio y dentro vamos a crear el fichero Vagrantfile, podemos crear uno vacio con la instrucción:::
        
	usuario@maquina:~/vagrant$ vagrant init
        
2. Modificamos el fichero Vagrantfile y los dejamos de la siguiente manera:::

    # -*- mode: ruby -*-
    # vi: set ft=ruby :
    Vagrant.configure("2") do |config|
                config.vm.box = "precise64"
                config.vm.hostname = "mimaquina"
                config.vm.network :public_network,:bridge=>"eth0"
    end    
    
3. Iniciamos la máquina:::

    usuario@maquina:~/vagrant$ vagrant up
        
4. Para acceder a la instancia:::
  	
    usuario@maquina:~/vagrant$ vagrant ssh default
    	      
5. Suspender, apagar o destruir:
    	
    usuario@maquina:~/vagrant$ vagrant suspend
    usuario@maquina:~/vagrant$ vagrant halt
    usuario@maquina:~/vagrant$ vagrant destroy

* **Práctica 4: Creación de varias máquinas virtuales**

En esta ocasión vamos a crear otro directorio y dentro un fichero Vagrantfile con el siguiente contenido:::

    # -*- mode: ruby -*-
    # vi: set ft=ruby :
    
    Vagrant.configure("2") do |config|
    
      config.vm.define :nodo1 do |nodo1|
        nodo1.vm.box = "precise64"
        nodo1.vm.hostname = "nodo1"
        nodo1.vm.network :private_network, ip: "10.1.1.101"
      end
      config.vm.define :nodo2 do |nodo2|
        nodo2.vm.box = "precise64"
        nodo2.vm.hostname = "nodo2"
        nodo2.vm.network :public_network,:bridge=>"eth0"
        nodo2.vm.network :private_network, ip: "10.1.1.102"
      end
    end

Cuando iniciemos el escenario veremos que hemos creado dos máquinas virtuales: nodo1 y nodo2. 
nodo1 tendrá una red interna con ip 10.1.1.101, y nodo2 tendrá una interfaz de red "modo puente" y una interfaz de red del tipo red interna con ip 10.1.1.102.

Si accedemos por ssh a nodo1 podremos hacer ping a nodo2.



Enlaces interesantes
--------------------

* `Página oficial de Vagrant <http://www.vagrantup.com/>`_
* `Gestionando máquinas virtuales con Vagrant <http://www.josedomingo.org/pledin/2013/09/gestionando-maquinas-virtuales-con-vagrant/>`_
* `Boxes oficiales para Vagrant <https://atlas.hashicorp.com/boxes/search>`_
* `Boxes no oficiales de Vagrant <http://www.vagrantbox.es/>`_
