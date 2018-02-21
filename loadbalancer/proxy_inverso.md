# Proxy inverso

## Configuración del proxy visto en clase

	ProxyPass "/ejercicio1/"  "http://ejercicio.gonzalonazareno.org/"
    ProxyPassReverse "/ejercicio1/"  "http://ejercicio.gonzalonazareno.org/"
    ProxyHTMLURLMap http://ejercicio.gonzalonazareno.org /ejercicio1
    <Location /ejercicio1/>
        ProxyPassReverse /
        ProxyHTMLEnable On
        ProxyHTMLURLMap / /ejercicio1/
        RequestHeader    unset  Accept-Encoding
    </Location>

Referencia: [http://www.apachetutor.org/admin/reverseproxies](http://www.apachetutor.org/admin/reverseproxies)