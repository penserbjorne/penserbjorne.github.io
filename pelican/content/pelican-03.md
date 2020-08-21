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
configuración.

Recordemos cual es la estructura de trabajo que tenemos hasta este momento:

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
        │   └── hola-mundo.md # Entrada nueva
        ├── output
        ├── tasks.py
        ├── Makefile
        ├── pelicanconf.py
        └── publishconf.py
```

Si observamos detenidamente, podemos ver que los archivos de los que hablamos se encuentran en nuestra subcarpeta `pelican` y son:

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
# Elimina los archivos generados previamente
invoke clean

# Genera el sitio para ver en local
invoke build

# Genera el sitio para ver en local eliminando previamente los archivos generados
invoke rebuild

# Regenera el sitio para ver en local cada vez que se hace un cambio
invoke regenerate

# Permite visualizar el sitio de manera local en http://localhost:8000/
invoke serve

# Genera el sitio para ver en local
# y luego lo permite visualizar de manera local en http://localhost:8000/
invoke reserve

# Genera el sitio para producción
invoke preview

# Permite visualizar el sitio de manera local en http://localhost:8000/
# y regenrar el sitio cada vez que haya un cambio, todo para local
invoke livereload

# Permite subir el sitio al servidor correspondiente mediante rsync y SSH
invoke publish

# Publica el sitio de producción en Github Pages
invoke gh-pages
```

Considerar que para el comando `invoke livereload` se requiere instalar la
herramienta `livereload` y para el comando `invoke gp_pages` se requiere la
herramienta `ghp-import`, esto lo podemos hacer mediante el siguiente comando:

```bash
python -m pip install livereload ghp-import
```

A partir de ahora estaremos trabajando con los comandos previos. Ahora, estos
comandos requieren algunas configuraciones, por ejemplo, los comandos asociados
a generar el sitio están configurados para generar los archivos dentro de una
carpeta llamada `output` la cual se encuentra al mismo nivel que la carpeta
`pelican`. En nuestro caso como estamos trabajando con un blog para un usuario
de `GitHub` por lo que necesitamos que los archivos sean generados en el
directorio raíz del repositorio, esto es una carpeta mas arriba de donde estamos
actualmente (recuerda que estamos en la carpeta `pelican`).

También vamos a modificar algunas de las tareas que vienen en el archivo
`tasks.py`.

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

# Modificando el pipeline de construcción del sitio

Ok, ya tenemos instaladas las herramientas para construir el sitio y hemos
configurado algunas variables que que tenga un poco más de personalidad el
sitio, eso significa que podemos generarlo.

Los pasos a ir siguiendo son sencillos y deben estar pensados en dos momentos:
desarrollo y producción.

Durante el desarrollo queremos ir viendo los cambios que vamos realizando en
local, así que podemos utilizar:

```bash
# Limpiamos archivos previos
invoke clean
# Comenzamos a generar sobre el vuelo
invoke livereload
```

Cuando hemos terminado de probar queremos construir el sitio para producción y
enviarlo a nuestro repositorio de `GitHub`, por lo que podemos utilizar:

```bash
# Limpiamos archivo previos
invoke clean
# Generamos versión de producción y publicamos actualizaciones
invoke gh-pages
```

Pero tenemos un problema, la tarea `clean` va a borrar todo en el contenido de
salida, esto incluiría la carpeta `pelican` por lo cual perderíamos los archivos
fuente del blog. Hay que modificar esta tarea :)

Y como queremos que todo quede en un solo comando tanto para producción como
para publicar el sitio vamos a hacer algunos cambios más que veremos a
continuación.

Para modificar las tareas nos vamos a dirigir al archivo `tasks.py`

##  Modificando la tarea `clean`

Vamos a comentar las lineas que se encuentran dentro de la tarea y las vamos a
reemplazar por el siguiente segmento de código:

```python
if os.path.isdir(CONFIG['deploy_path']):
      c.run('rm -rf ../author ../category ../drafts ../feeds ../tag ../theme '
              '../*.html')
```

De tal modo que la tarea se vería más o menos así:

```python
@task
def clean(c):
    """Remove generated files"""
    # Old code
    #if os.path.isdir(CONFIG['deploy_path']):
    #    shutil.rmtree(CONFIG['deploy_path'])
    #    os.makedirs(CONFIG['deploy_path'])

    #My own code
    if os.path.isdir(CONFIG['deploy_path']):
        c.run('rm -rf ../author ../category ../drafts ../feeds ../tag ../theme '
                '../*.html')
```

##  Modificando la tarea `livereload`

Queremos que cada vez que se haga un `livereload` también se limpien los
archivos generados previamente, por lo cual vamos a añadir la tarea `clean`
dentro de `livereload`, para esto solamente añadiremos la linea `clean(c)` antes
`build(c)`, de tal modo que la tarea quedaría así:

```python
@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    clean(c)    # New line, added by me :)
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured port
    server.serve(port=CONFIG['port'], root=CONFIG['deploy_path'])
```

##  Modificando la tarea `gh-pages`

De igual manera  que en la tarea anterior, simplemente vamos a añadir la linea
de `clean(c)` para verificar que no haya basura. La linea a añadir la ubicaremos
antes de la linea `preview(c)`.

Y por alguna razón en este momento estamos teniendo problemas con `ghp-import`
por lo que vamos a añadir lo siguiente:

```python
```

La tarea quedaría de la siguiente manera:

```python
@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    clean(c)
    preview(c)

    # Old code
    #c.run('ghp-import -b {github_pages_branch} '
    #      '-m {commit_message} '
    #      '{deploy_path} -p'.format(**CONFIG))

    # My code
    c.run('git add --all'.format(**CONFIG))
    c.run('git commit -m {commit_message}'.format(**CONFIG))
    c.run('git push'.format(**CONFIG))
```

Podemos ver que el nombre de la función dentro de `tasks.py` lleva guion bajo
mientras que al utilizarlo con `invoke` lleva guion medio, esto no sé porque
sea pero hay que dejarlo así.

Y consideremos que dentro del archivo `tasks.py` existen las variables `github_pages_branch` y `commit_message` que son a las que se hace referencia
en la tarea.

##  Pasos resultantes para construir el sitio

Con los cambios anteriores nuestro pequeño ciclo de desarrollo quedaría:

```bash
# Desarrollo
invoke livereload

# Producción
invoke gh-pages
```

Con esto hemos automatizado un poco nuestro pequeño ciclo de desarrollo del
sitio.

Para ver el archivo `tasks.py` de este blog puedes dar click
[aquí](https://github.com/penserbjorne/penserbjorne.github.io/blob/master/pelican/tasks.py)

# Siguientes pasos

Ya tenemos nuestro sitio con un poco mas de estilo, sin embargo sigue sin ser
responsivo por lo cual no es fácil de leer en dispositivos con pantallas
medianas o pequeñas, el siguiente paso es configurar un tema responsivo, pero
esto lo haremos en la siguiente entrada :)

Que la fuerza te acompañe.
