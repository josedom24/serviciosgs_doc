Python para sysadmins
=====================

Para automatizar muchas de las tareas que realizan los administrador de sistemas es necesario crear scripts. Éstos se pueden crear en distintos lenguajes de programación, por ejemplo bash. En este apartado vamos a introducir las posibilidades que nos ofrece python para crear script de administración.

.. note:: Si quieres más información puedes consultar la página `Python for system administrators <http://www.ibm.com/developerworks/aix/library/au-python/>`_.

Resumen de instrucciones
------------------------

Veamos algunas instrucciones que nos pueden ayudar en nuestrs scripts de administración:

* **Trabajar con argumentos en la línea de comandos**: La mayoría de los script que realicemos recibiran la entrada por argumentos de la línea de comandos.::

	import sys
	len (sys.argv) #Número de argumentos
	sys.argv[1] #Acceso al segundo argumento

* **Salir del programa**: Nos puede interesar que el programa termine baja alguna circunstancia.::

	import sys
	sys.exit(0)

* **La libreía *os* te permite acceder del sistema operativo**: Esta librería es muy importante para realizar scripts de administración, veamos algunos ejemplos.::

	import os
	print os.getcwd() #Devuelve el directorio donde estás trabajando
	os.chdir("Descargas") #Cambia de directorio
	os.system("clear") #Ejecuta una instrucción pero no podemos obtener el resultado

* **Ejecutar una instrucción y obtener el resultado**: Tenemos tres posibilidades.::

	#Utilizando la librería commands
	import commands
	data = commands.getoutput("ls -l")
	type(data)
	lineas=data.split("\n")

	#Otra manera, pero poco "elegante"
	os.system("ls -l>tmp.txt")
	f=open("tmp.txt","r")

	#Ejecutar la instrucción como si fuera un fichero
	f=popen("ls -l","r")