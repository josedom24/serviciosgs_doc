#-*- coding: utf-8 -*-

import os
import time
import commands

# Configuración
CONN =[1,10,25,50,75,100]
TITULO="modulo"
DURATION="10"
IP="localhost"
URLS=["wordpress/","wordpress/index.php/2017/11/20/hello-world/","wordpress/?s=hola","wordpress/index.php/2017/11/"]
SERVERS=["apache2","memcached"]

##############################################################################################################
resultados=[]
for con in CONN:
        lcon=[]
        print("Conexiones concurrentes %d"%con)
        for url in URLS:
                print("URL: http://%s/%s"%(IP,url))
                res=commands.getoutput('ab -t %s -k -c %s http://%s/%s | grep "Requests per second:"|awk \'{print $4}\''%(DURATION,con,IP,url))
                try:
                        lcon.append(float(res.split("\n")[-1]))
                except:
                        pass
        resultados.append(lcon)
        for server in SERVERS:
                print "Reiniciando %s..." % server
                os.system("systemctl restart %s" % server)
cad=TITULO+","
for lista in resultados:
        if len(lista)<3:
                cad+=str(sum(lista)/len(lista))
        else:
                cad+=str(sum(sorted(lista)[1:-1])/len(sorted(lista)[1:-1]))
        cad+=","
print cad[:-1]
