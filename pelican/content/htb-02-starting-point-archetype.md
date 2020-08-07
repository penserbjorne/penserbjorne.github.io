---
Title: Hack-The-Box > Starting point > Archetype
Date: 2020-08-06
Modified: 2020-08-06
Tags: blog, penserbjorne, htb, pentest, hacking, archetype
Keywords: blog, penserbjorne, htb, pentest, hacking, archetype
Category: htb
Author: penserbjorne
Summary: Anotaciones sobre la maquina "Archetype" de la sección "Starting point" de Hack-The-Box
Lang: es-MX
Translation: false
Status: published
---

# Archetype

Para comenzar con esta serie de anotaciones sobre la sección *Starting point*
arrancaremos con la máquina *Archetype*. Si no sabes bien de que hablo te
recomiendo que primero leas la
[entrada anterior]({filename}./htb-01-starting-point-section.md).

- **Maquina:** Archetype
- **SO:** Windows
- **IP:** 10.10.10.27

## Enumeration

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
los puertos abiertos en la maquina a trabajar. Esto se lo indicamos a `nmap`
con los siguientes parámetros:

- `-p-`: Indicamos que vamos a escanear todos los puertos de la maquina.
- `--min-rate=1000`: Indicamos que enviaremos al menos 1000 paquetes por segundos para realizar el escaneo.
- `-T4`: Indicamos una *plantilla de tiempo*. Básicamente le decimos a `nmap`
que los tiempos haga un *análisis agresivo*. El modo agresivo hace que los
análisis sean más rápidos al asumir que estas en una red razonablemente más
rápida y fiable.
- `10.10.10.27`: Indicamos la IP del objetivo, en este caso es la maquina con la que vamos a trabajar.

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
utilizar en el comando siguiente:

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

---

Por ahora el post quedara hasta aquí ... tengo hambre y necesito descansar un
rato.

`#HappyHacking`
