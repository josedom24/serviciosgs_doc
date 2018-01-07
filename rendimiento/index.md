# Gestión de peticiones y rendimiento en servidores Web


Los servidores web pueden ser configurado para manejar las peticiones de diferente forma, desde el punto de vista en que son creados y manejados los subprocesos necesarios que atienden a cada cliente conectado a este. En esta unidad vamos a explicar los MPM (Módulos de multiprocesamiento) que nos permiten configurar el servidor Web para gestionar las peticiones que llegan al servidor.

Vamos a estudiar tambíen las distintas configuraciones que podemos realizar para que los servidores web sean capaces de servir páginas realizadas en PHP y Python y vamos a estudiar las diferencias de rendimientos (respuestas por segundos) que podemos obtener utilizando las distintas configuraciones. Por último estudiaremos diferentes aplicaciones que pueden mejorar el rendimiento de nuetro servidor: aceleradores PHP, memcache, varnish, ...

Para terminar la unidad vamos a hacer un estudio comparativo sobre el rendimiento entre distintos servidores web.

```eval_rst
.. toctree::
   
   enlaces
   ejercicio1
   script_php
   php
   
