---
Title: Hack-The-Box > Starting point > Archetype
Date: 2020-08-06
Modified: 2020-08-11
Tags: blog, penserbjorne, htb, pentest, hacking, archetype
Keywords: blog, penserbjorne, htb, pentest, hacking, archetype
Category: htb
Author: penserbjorne
Summary: Anotaciones sobre la máquina "Archetype" de la sección "Starting point" de Hack-The-Box
Lang: es-MX
Translation: false
Status: published
---

# Archetype

Para comenzar con esta serie de anotaciones sobre la sección *Starting point*
arrancaremos con la máquina *Archetype*. Si no sabes bien de que hablo te
recomiendo que primero leas la
[entrada anterior]({filename}./htb-01-starting-point-section.md).

- **máquina:** Archetype
- **SO:** Windows
- **IP:** 10.10.10.27

## Enumeration

Como siempre digo: "*primero lo primero*", pues vamos a comenzar a **enumerar**
lo que tiene el equipo objetivo, en este caso vamos a tratar de identificar
los puertos abiertos y el software asociado a estos.

Para esto utilizaremos la siempre poderosa herramienta de
[Nmap](https://es.wikipedia.org/wiki/Nmap).

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
que los tiempos haga un *análisis agresivo*. El modo agresivo hace que los
análisis sean más rápidos al asumir que estas en una red razonablemente más
rápida y fiable.
- `10.10.10.27`: Indicamos la IP del objetivo, en este caso es la máquina con la que vamos a trabajar.

La salida del comando anterior nos muestra la lista de puertos abiertos como
se ve a continuación.

```bash
└──╼ $nmap -p- --min-rate=1000 -T4 10.10.10.27
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
solamente el listado de puertos sin la información de `nmap`. Esto se lo
indicamos a `grep` utilizando la expresión regular `^[0-9]` la cual
especifica que busque las lineas que comienzan con valores numéricos que van
del 0 al 9. La salida es como se muestra a continuación.

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
carácter para *separar* la cadena en *columna*, Algo así como la coma *,* de
un CSV.
- `-f 1`: Indicamos que retorne o imprima el primer campo de los resultados.
En este caso si observamos la salida del comando anterior podemos asumir que
las lineas de texto se van a separar en dos columnas debido a que cada linea
tiene el carácter `/`. El primer campo tendrá el número de puerto y el segundo
campo tendrá la descripción del puerto.

La salida sel comando anterior es la siguiente:

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
Esto lo hacemos con la expresión `s/,$//` la cual se pasa a `sed` y respeta
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
[Samba](https://es.wikipedia.org/wiki/Samba_(software)) en sistemas tipo Unix.

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
(`\\\\`), por eso al ver al inicio cuatro barras invertidas y dos al inicio, en
realidad la sintaxis de `DOS` lo tomaría como dos barras al inicio y una al
final.

El resultado del comando anterior es:

```bash
└──╼ $smbclient -N -L \\\\10.10.10.27\\

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	backups         Disk      
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
SMB1 disabled -- no workgroup available
```

Revisando la salida del comando podemos observar que hay una carpeta interesante
llamada `backup` la cual podria contener información interesante. Procederemos
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
son archivos de configuración con sintaxis `XML` utilizados en para aplicar
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

```bash
└──╼ $cat prod.dtsConfig
```
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

La cadena anterior corresponde a la cadena para una conexión SQL asociada al
usuario `ARCHETYPE\sql_svc` y su contraseña que es `M3g4c0rp123`.

## Foothold

Ya tenemos un usuario y contraseña, por lo que podemos intentar dar un primer
paso firme hacia nuestra máquina objetivo ... peeeeero, eso será después porqué
en este momento necesito dejar el post pausado una vez más y conectarme a hacer
algunos pendientes del trabajo :)

`#HappyHacking`
