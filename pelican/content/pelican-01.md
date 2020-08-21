---
Title: Pelican (01), creación de un blog estático con Pelican
Date: 2020-04-24
Modified: 2020-08-20
Tags: blog, pelican
Keywords: blog, pelican
Category: pelican
Author: Penserbjorne
Summary: Creación de un blog estático con Pelican
Lang: es-MX
Translation: false
Status: published
---

# What is this?

Bueno, como primera entrada de notas, lo más lógico (para mi) es comenzar con la
herramienta que esta haciendo posible esto, `Pelican`. Esto ira siendo una serie
de entradas sobre como trabajar con `Pelican`, por ahora nos enfocaremos en
crear el sitio.

[Pelican](https://blog.getpelican.com/) es una herramienta para generar sitios
estáticos que no requieren una base de datos o una lógica en el lado del
servidor.

Básicamente, elegí `Pelican` por "simplicidad":

- Instalamos las herramientas necesarias de `Pelican`.
- Escribimos en `Markdown`.
- Generamos los archivos del sitio.
- Publicamos el sitio en el servidor.

Estos pasos son "sencillos" si estas acostumbradx a manejar herramientas
en un terminal (la famosa ventanita negra), el cual, es mi caso.

So, en esta entrada iré añadiendo las cosas que considero necesito tener a la
mano para administrar el blog. Toda la documentación necesaria (y extendida) se
encuentra en [el blog oficial de Pelican](https://docs.getpelican.com), por lo
que si se necesita mayor información o detalle de algo, visitar el sitio oficial
(recuerda siempre, **\#RTFM**).

En este momento me encuentro trabajando en un equipo con `Lubuntu 18.04` por
lo cual las instrucciones de instalación serán para esta distribución.

# Preparación del entorno

Dado que `Pelican` es una herramienta desarrollada con `Python` y lo mejor es
buscar tener un entorno limpio, estaremos trabajando con `virtualenv`.

```bash
# Instalación del entorno
sudo apt install virtualenv

# Creación del entorno
virtualenv ~/path/to/project
```

Para comenzar a trabajar es necesario movernos a la carpeta donde se configuró
el entorno y activarlo.

```bash
# Nos movemos a la carpeta creada
cd ~/path/to/project

# Activamos el entorno
source bin/activate
```

Sabremos que el entorno se ha activado por que la terminal cambiará su apariencia
a algo como lo siguiente.

```bash
(entorno_virtual) usuario@equipo:~/path/to/project$
```

A partir de aquí podemos comenzar a trabajar con `Pelican` en un entorno aislado
que no vaya a modificar nuestro sistema operativo.

Una vez que hayamos terminado de trabajar en el sitio, podemos desactivar el
entorno.

```bash
# Para desactivar virtualenv
deactivate
```

# Instalación de las herramientas

En este caso vamos a redactar el sitio en `Markdown`, por lo cual instalaremos
lo necesario para que `Pelican` funcione con `Markdown`. Esto lo haremos a
través de `pip` **\#PorquePython**.

Necesitaremos los paquetes de `pelican`, `Markdown` y `typogrify`.

```bash
pip install pelican Markdown typogrify
```

En caso de necesitar actualizar alguna de estas herramientas, se puede hacer
también a través de `pip`.

```bash
pip install --upgrade pelican Markdown typogrify
```

# Creación del esqueleto del sitio

Para crear un proyecto con la estructura básica de `Pelican` basta con ejecutar
el siguiente comando (aún no lo hagas, necesito aclarar algo antes).

```bash
pelican-quickstart
```

El comando creara una carpeta con la siguiente estructura:

```bash
yourproject/
├── content
│   └── (pages)
├── output
├── tasks.py
├── Makefile
├── pelicanconf.py
└── publishconf.py
```

Como podemos ver, es una estructura bien definida para el sitio. Esta estructura
es la que se encontrará alojada en el repositorio del sitio. Hay que tener en
cuenta que actualmente estamos en la carpeta de `virtualenv`, así que aquí es
donde vamos a clonar el repositorio, de tal modo que la carpeta actual tendría
que verse así (asumiendo que ya clonamos el repositorio dentro de la carpeta de
  virtualenv ¬¬):

```bash
(entorno_virtual) usuario@equipo:~/path/to/project$ ls
bin  include  lib  local  user.github.io  share
```

Como podemos observar, están las carpetas de `virtualenv` y el repositorio del
sitio, que en todo caso, si no es un repositorio, valdría la pena crear una
carpeta (por ejemplo blog),  para que esta no se mezcle con lo de `virtualenv`.

Básicamente estamos separando `virtualenv` y el repositorio en carpetas
distintas, para evitar que nuestro entorno virtual se vaya al repositorio.

Dentro de la carpeta del repositorio será necesario crear una subcarpeta más. En
esta carpeta que llamaremos `pelican` es donde se encontrara los archivos fuente
del sitio que son con los que trabaja `Pelican`, y dentro de esta subcarpeta es
donde ejecutaremos el comando para la creación del proyecto (ya sé, ya sé,
  tanta carpeta marea, pero hay una razón para hacerlo así, por ahora confiá
  en mi).

```bash
(entorno_virtual) usuario@equipo:~/path/to/project/user.github.io/pelican$ pelican-quickstart
```

De tal modo que la estructura de archivos debería de verse de la siguiente
manera.

```bash
/path/to/project
├── bin/          # carpeta de virtualenv
├── include/      # carpeta de virtualenv
├── lib/          # carpeta de virtualenv
├── local/        # carpeta de virtualenv
├── share/        # carpeta de virtualenv
└── user.github.io/   # carpeta del repositorio del sitio
    └── pelican/      # carpeta con los archivos fuente del sitio
        ├── content             
        │   └── (pages)
        ├── output
        ├── tasks.py
        ├── Makefile
        ├── pelicanconf.py
        └── publishconf.py
```

# Generar y ejecutar el sitio

Para generar el contenido del sitio vamos a posicionarnos en la carpeta del
repositorio (o la que hemos llamado blog).

`Pelican` cuenta con el comando `pelican content`, el cual revisa los archivos
necesarios para generar la salida de `HTML`. La salida se almacena en automático
en una carpeta llama `output`.

En nuestro caso como estamos utilizando `GihHub Pages` tenemos la restricción de
que el contenido sel sitio tiene que encontrarse en la raíz del repositorio en
la rama `master`, por lo cual tenemos que indicar que la salida sea en la raíz
del repositorio (ves! así tenemos la salida del sitio en la raíz del
  repositorio y los archivos fuente en la subcarpeta `pelican`).

Para lo anterior (y estando en la subcarpeta `pelican`) ejecutamos:

```bash
# Generamos la salida HTML una carpeta arriba de donde estamos
pelican content -o ..
```

Esto generara los archivos `HTML` del sitio en la raíz del repositorio.

Para visualizar el sitio contamos con el comando `pelican --listen` el cual
levanta un servidor en el puerto 8080. En nuestro caso (y sin salir de la
  subcarpeta) tendremos que indicar donde estan los archivos generados, por lo
  cual vamos a ejecutar el siguiente comando:

```bash
# Levantamos el sitio indicando la salida de los archivos HTML
pelican --listen -o ..
```

Para acceder al sitio visitamos [http://localhost:8000/](http://localhost:8000/)
, y listo, tendríamos que observar el sitio andando.

Para poder estar trabajando con el sitio, es necesario cada vez que hagamos un
cambio o modificación volver a generar los archivos.

# Creación de contenido

Recordando la estructura del sitio, sabemos que las entradas del mismo
van en la carpeta `content` de nuestra subcarpeta `pelican`. Ahí es donde
podremos comenzar a crear nuestros archivos en `Markdown`. Esto lo dejaremos
para la siguiente entrada, es momento de pararse por un poco de agua, algo de
comer y a estirar la espalda y las piernas.
