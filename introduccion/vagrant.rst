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


Enlaces interesantes
--------------------

* `Página oficial de Vagrant <http://www.vagrantup.com/>`_
* `Gestionando máquinas virtuales con Vagrant <http://www.josedomingo.org/pledin/2013/09/gestionando-maquinas-virtuales-con-vagrant/>`_
* `Boxes oficiales para Vagrant <https://atlas.hashicorp.com/boxes/search>`_
* `Boxes no oficiales de Vagrant <http://www.vagrantbox.es/>`_
