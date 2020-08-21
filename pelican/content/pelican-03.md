---
Title: Pelican (03), configuración del sitio (construcción y elementos básicos)
Date: 2020-08-20
Modified: 2020-08-21
Tags: blog, pelican
Keywords: blog, pelican
Category: pelican
Author: Penserbjorne
Summary: Configuración para construir y asignar elementos básicos de un sitio con Pelican
Lang: es-MX
Translation: false
Status: published
---

# What is this?

Ok, esta es la tercera entrada para trabajar generando un sitio con `Pelican` en
`gh-pages`. En esta ocasión vamos modificar algunas configuraciones para probar
y construir el sitio, así como asignarle un tema.

Te recomendamos revisar las entradas anteriores en donde fuimos construyendo
el sitio sobre el que vamos a trabajar ahora.
[Creación de un blog estático con Pelican]({filename}./pelican-01.md)
y
[Creación de entradas para un blog estático con Pelican]({filename}./pelican-02.md)

Como ya hemos dicho, toda la documentación necesaria (y extendida) se
encuentra en [el blog oficial de Pelican](https://docs.getpelican.com), por lo
que si se necesita mayor información o detalle de algo, visitar el sitio oficial
(recuerda siempre, **\#RTFM**).

# Archivos de configuración

Cuando comenzamos a crear el sitio utilizamos el comando `pelican-quickstart`
el cual nos creo la estructura inicial del sitio con algunos archivos de
configuración. Estos archivos de configuración son:

- `Makefile`
- `pelicanconf.py`
- `publishconf.py`
- `tasks.py`

En los archivos `pelicanconf.py` y `publishconf.py` vamos a indicar las
variables de configuración para el sitio.

Con los archivos `Makefile` y `tasks.py` vamos a indicar las acciones necesarias
para construir el sitio.

# Construcción del sitio

Como recordaras para construir el sitio y previsualizarlo hemos estado
utilizando los siguientes comandos:

```bash
# Generamos la salida HTML una carpeta arriba de donde estamos
pelican content -o ..

# Levantamos el sitio indicando la salida de los archivos HTML
pelican --listen -o ..
```

Estos comando los podemos sustituir utilizando la herramienta
[invoke](https://www.pyinvoke.org/) o la herramienta
[make](https://www.gnu.org/software/make/).

En este caso vamos a trabajar con `invoke` solo para variarle un poco, si te
interesa leer la versión completa o con `make` puedes
[dar click aquí](https://docs.getpelican.com/en/stable/publish.html).

Para trabajar con `invoke` necesitamos instalarlo a través de `pip`. Recuerda
hacerlo después de haber activado el entorno virtual que creamos en
[la primera entrada]({filename}./pelican-01.md) y de haber entrado a la carpeta
`pelican` que se encuentra dentro del repositorio.

Para instalar `invoke` podemos ejecutar lo siguiente:

```bash
python -m pip install invoke
```

Lo divertido de `invoke` es que funciona utilizando el archivo `tasks.py`
el cual contiene *tareas* definidas a ejecutar, básicamente es un archivo en
el que podemos automatizar tareas mediante `python`.

Afortunadamente el archivo `tasks.py` que tenemos ya tiene las tareas definidas
por lo cual podemos trabajar en automático con este archivo o modificarlo para
adaptarlo a nuestras necesidades.

Los comandos que vienen precargados en el archivo `tasks.py` son:

```bash
# Genera el sitio, convierte de Markdown a HTML
invoke build

# Regenera el sitio cada vez que se hace un cambio
invoke regenerate

# Permite visualizar el sitio de manera local en http://localhost:8000/
invoke serve

# Permite visualizar el sitio de manera local en http://localhost:8000/
# y regenrar el sitio cada vez que haya un cambio
invoke livereload

# Permite subir el sitio al servidor correspondiente mediante SSH
invoke publish
```

Considerar que para el comando `invoke livereload` se requiere instalar la
herramienta `livereload`, esto lo podemos hacer mediante el siguiente comando:

```bash
python -m pip install livereload
```

A partir de ahora estaremos trabajando con los comandos previos. Ahora, estos
comandos requieren algunas configuraciones, por ejemplo, los comandos asociados
a generar el sitio están configurados para generar los archivos dentro de una
carpeta llamada `output` la cual se encuentra al mismo nivel que la carpeta
`pelican`. En nuestro caso como estamos trabajando con un blog para un usuario
de `GitHub` por lo que necesitamos que los archivos sean generados en el
directorio raíz del repositorio, esto es una carpeta mas arriba de donde estamos
actualmente (recuerda que estamos en la capreta `pelican`).

# Configuración de variables del sitio

Bien, ya vimos que comandos vamos a estar utilizando y ya mencionamos que
necesitamos configurarlos, esto lo vamos a hacer en los archivos
`pelicanconf.py` y `publishconf.py`.

El archivo `pelicanconf.py` es utilizado para trabajar en el desarrollo local
del sitio mientras que `publishconf.py` es utilizado para producción. El archivo
`pelicanconf.py` es llamado en `publishconf.py` por lo cual las variables que se
encuentren en el segundo reescriben a las variables del primero. Por ejemplo,
si la variable `SITEURL` se encuentra asignada en ambos archivos, la de
`publishconf.py` sobreescribe a la de `pelicanconf.py`.

La lista de variables y su descripción la puedes encontrar
[aquí](https://docs.getpelican.com/en/stable/settings.html). Te recomiendo leer
este listado ya que aquí abordaremos solo algunas variables para configurar los
comando anteriores y el tema del sitio.

## Directorio de salida

Para modificar el directorio de salida necesitamos modificar la variable
`OUTPUT_PATH` la cual tiene el valor predeterminado de `'output/'`, en este caso
vamos a modificar la variable para que el directorio de salida sea en un nivel
superior a la ruta actual por lo cual variable quedará como
`OUTPUT_PATH = './../'`.

Esta variable hay que asignarla en `pelicanconf.py`.

## Algunas otras configuraciones sencillas del sitio :D

Bien, ya hemos modificado la ruta de salida, por lo que podemos configurar
otras variables que le dan más vida al sitio.

Las siguientes variables las configuraremos en `pelicanconf.py`:

- `AUTHOR`: Nombre del autor del sitio
- `SITENAME`: Nombre del sitio
- `SITESUBTITLE`: Subtitulo del sitio
- `TYPOGRIFY`: La asignaremos como `True` para procesar las tipografías y el
texto del sitio y que tengan mejor presentación.
- `GITHUB_URL`: URL para el perfil de `GitHub`, aparecerá un botón para hacer
fork al sitio.
- `LINKS`: Literalmente es una lista de enlaces que quieres que aparezcan en el
sitio.
- `SOCIAL`: La lista de enlaces a tus redes sociales.

Tanto la sintaxxis de `LINKS` como la de `SOCIAL` es la siguiente:

```bash
VARIABLE = (('enalce 1', 'http://url-1.com/'),
            ('enalce 2', 'http://url-2.com/'),
            ('enalce 3', 'http://url-3.com/'),)
```


Las siguientes variables las configuraremos en `publishconf.py`:

- `SITEURL`: URL del sitio, tiene que incluir http o https al inicio, por
ejemplo https://sitio.com
- `DELETE_OUTPUT_DIRECTORY`: Dado que no queremos eliminar el directorio de
salida ya que ahí se encuentra nuestra carpeta de `pelican` vamos a cambiar su
valor a `False`.

Recuerda que las variables tienen un formato de `VARIABLE = valor`. El nombre
de la variable va en mayúsculas seguida de un espacio, el símbolo de `=`, otro
espacio y el valor de la variable.

Si quieres ver como van quedando los archivos de configuración de este sitio
puedes revisar el [aquí (pelicanconf.py)](https://github.com/penserbjorne/penserbjorne.github.io/blob/master/pelican/pelicanconf.py) y
[aquí (publishconf.py)](https://github.com/penserbjorne/penserbjorne.github.io/blob/master/pelican/publishconf.py).

# Siguientes pasos

Ya tenemos nuestro sitio con un poco mas de estilo, sin embargo sigue sin ser
responsivo por lo cual no es fácil de leer en dispositivos con pantallas
medianas o pequeñas, el siguiente paso es configurar un tema responsivo, pero
esto lo haremos en la siguiente entrada :)

Que la fuerza te acompañe.
