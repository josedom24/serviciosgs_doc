# Introducción a vagrant

Vagrant es una aplicación libre desarrollada en ruby que nos permite crear y personalizar entornos de desarrollo livianos, reproducibles y portables. Vagrant nos permite automatizar la creación y gestión de máquinas virtuales. Las máquinas virtuales creadas por vagrant se pueden ejecutar con distintos gestores de máquinas virtuales (oficialmente VirtualBox, VMWare e Hyper-V), en nuestro ejemplo vamos a usar máquinas virtuales en VirtualBox.

El objetivo principal de vagrant es aproximar los entornos de desarrollo y producción, de esta manera el desarrollador tiene a su disposición una manera  muy sencilla de desplegar una infraestructura similar a la que se va a tener en entornos de producción. A los administradores de sistemas les facilita la creación de infraestructuras de prueba y desarrollo.

[Presentación: Vagrant y ansible. Una combinación explosiva (1ª parte)](http://iesgn.github.io/cloud/curso/u2/presentacion_vagrant)

## Práctica con vagrant

* **Práctica 1: Instalación de vagrant**

Instalar virtualbox y vagrant:

    ```bash
    root@maquina:~$ apt-get install virtualbox
    root@maquina:~$ wget https://releases.hashicorp.com/vagrant/1.8.5/vagrant_1.8.5_x86_64.deb
    root@maquina:~$ dpkg -i vagrant_1.8.5_x86_64.deb
    ```

