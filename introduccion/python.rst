Python para sysadmins
=====================

Para automatizar muchas de las tareas que realizan los administrador de sistemas es necesario crear scripts. Éstos se pueden crear en distintos lenguajes de programación, por ejemplo bash. En este apartado vamos a introducir las posibilidades que nos ofrece python para crear script de administración. 


..note:: Si quieres más információn puedes consultar la página `Python for system administrators <http://www.ibm.com/developerworks/aix/library/au-python/>`_)

Resumen de instrucciones
------------------------

Veamos algunas instrucciones que nos pueden ayudar en nuestrs scripts de administración:

* **Trabajar con argumentos en la línea de comandos**: La mayoría de los script que realicemos recibiran la entrada por argumentos de la línea de comandos.::

	import sys
	len (sys.argv) #Número de argumentos
	sys.argv[1] #Acceso al segundo argumento