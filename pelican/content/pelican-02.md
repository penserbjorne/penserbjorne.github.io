---
Title: Pelican (II), creación de entradas para un blog estático con Pelican
Date: 2020-05-09
Modified: 2020-05-09
Tags: blog pelican
Keywords: blog pelican
Category: pelican
Author: Penserbjorne
Summary: Creación de entradas para un blog estático con Pelican
Lang: es-MX
Translation: false
Status: published
---

# What is this?

Weno weno, ¿de que va esta entrada? Pues de cómo escribir contenido (entradas)
en el blog con `Pelican`. Esto es continuación de la
[entrada anterior]({filename}./pelican-01.md) en la cual vimos una ligera
introducción a `Pelican`, cómo instalarlo y como ejecutarlo para ver andando el
sitio.

Como ya hemos dicho, toda la documentación necesaria (y extendida) se
encuentra en [el blog oficial de Pelican](https://docs.getpelican.com), por lo
que si se necesita mayor información o detalle de algo, visitar el sitio oficial
(recuerda siempre, **\#RTFM**).

# Markdown

Una de las razones por las cuales elegimos `Pelican` como herramienta para
escribir el blog es que tiene soporte para `Markdown`.

`Markdown` a grandes rasgos es un lenguaje de marcado ligero, esto significa que
se escribe texto plano utilizando etiquetas que posteriormente serán convertidas
a un formato más bonito, en este caso HTML.

La ventaja de utilizar `Markdown` es que podemos enfocarnos simplemente en
escribir utilizando cualquier editor de texto (simple o tan complejo como tu
quieras) sabiendo que las etiquetas que estamos utilizando tendrán un
formato agradable de leer.

Si quieres aprender un poco más sobre `Markdown` te dejo su [entrada de
`Wikipedia`](https://es.wikipedia.org/wiki/Markdown),
[el sitio original de su publicación](https://daringfireball.net/projects/markdown/)
y una [sheetcheat de sus etiquetas](https://markdown.es/sintaxis-markdown/)
para que veas lo sencillo que es.

En este caso, la extensión del archivo `Markdown` que estaremos utilizando es
`.md`.

# ¿Donde vamos a escribir?

Recordando la estructura del sitio, sabemos que las entradas del mismo
van en la carpeta `content` de nuestra subcarpeta `pelican`. Ahí es donde
podremos comenzar a crear nuestros archivos en `Markdown`.

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

Por lo que para añadir una nueva entrada bastará con crear un archivo nuevo en
la carpeta `content` con la extensión `.md`

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

En este caso hemos agregado el archivo `hola-mundo.md`. Al ejecutar el comando
para generar el sitio `Pelican` tomara este archivo y lo procesara para darle
la salida necesaria y general el sitio.

Por lo tanto, para añadir más contenido a tu sitio basta con que lo agreguemos a
esta carpeta.

# ¿Qué debe llevar una entrada?

Para una gestión adecuada del contenido en el sitio `Pelican` necesita conocer
algunas cosas sobre el contenido que estamos generando. Para esto es necesario
incluir algunas etiquetas al inicio del archivo que serán consideradas como
`metadatos` por `Pelican`.

A continuación una tabla con las etiquetas y para que sirven:

| Metadata | Description |
| - | - |
| `title` | Titulo del artículo o de la página |
| `date` | Fecha de publicación (e.g., YYYY-MM-DD HH:SS) |
| `modified` | Fecha de modificación (e.g., YYYY-MM-DD HH:SS) |
| `tags` | Tags del contenido, separados por comas |
| `keywords` | Palabras claves del contenido |
| `category` | Categórica del contenido, solo una |
| `slug` | Identificador utilizado en URLs y en traducciones |
| `author` | Autor (uno) |
| `authors` | Autores (más de uno) |
| `summary` | Pequeña descripción del contenido del artículo |
| `lang` | Idioma (en, fr, etc.) |
| `translation` | Indicamos si es un contenido traducido (true or false) |
| `status`  | Estatus del contenido: borrador (draft), oculto (hidden), o publicado (published) |
| `template` | Nombre de la plantilla a utilizar para generar el contenido |
| `save_as` | Guardar el archivo con respecto a su dirección relativa |
| `url` | URL a utilizar para el artículo o página |

Para el caso de este blog, estamos utilizando las siguientes etiquetas:

```
---
Title: Este es el titulo
Date: 2020-05-09
Modified: 2020-05-09
Tags: blog pelican
Keywords: blog pelican
Category: pelican
Author: Penserbjorne
Summary: Descripción del texto
Lang: es-MX
Translation: false
Status: published
---
```

Estas etiquetas se encuentran al inicio de cada archivo y están contenidas entre
dos lineas de tres guiones medios `---` al inicio y al final, estas lineas no
son obligatorias.

En caso de no incluir estas etiquetas `Pelican` no podrá procesar el archivo ni
procederá a convertirlo.

# Ahora sí a escribir

Una vez que tenemos el archivo con su extensión `.md` y que le añadimos las
etiquetas necesarias podemos comenzar a escribir su contenido en `Markdown`.

Una vez que la entrada ha sido redactada podemos proceder a procesar el sitio
para que se genere el archivo de salida. Esto lo hacemos con los comandos que
vimos en la [entrada anterior]({filename}./pelican-01.md) (que te recomiendo leer para que
no te pierdas en la estructura de archivos y de trabajo que utilizamos aquí).

```bash
# Generamos la salida HTML una carpeta arriba de donde estamos
pelican content -o ..

# Levantamos el sitio indicando la salida de los archivos HTML
pelican --listen -o ..
```

Para acceder al sitio en local visitamos
[http://localhost:8000/](http://localhost:8000/), y listo, tendríamos que
observar el sitio andando con nuestra entrada nueva.

Para poder estar trabajando con el sitio, es necesario cada vez que hagamos un
cambio y modificación volver a generar los archivos.

# Consideraciones de trabajo

Cada vez que regeneremos el sitio porque hemos realizado un cambio o hemos
añadido contenido nuevo se van a generar los archivos `HTML` correspondientes,
si observamos cuidadosamente veremos que los archivos viejos no se eliminan.

Vamos a suponer que le cambiamos el nombre a una categoría o a un texto, sus
archivos correspondientes en la versión anterior seguirán ahí, por lo que hay
que limpiar el entorno de trabajo.

Por el momento una opción burda es eliminar todos los archivos y carpetas del
directorio raíz del repositorio y dejar exclusivamente la carpeta `pelican`.

Lo sé, lo sé, esto no es lo más viable o factible a largo plazo, ¡pero oye!
apenas vamos comenzando, por lo cual lo solucionaremos más adelante, por ahora
solo no te asustes si ves contenido duplicado, eliminalo y ya.

# Siguientes pasos

Ya tenemos nuestro primer `hola mundo` en el blog, basta con hacer push al repo
para poder verlo andando en nuestra `GitHub Pages`.

Esto es solo el comienzo, aún necesitamos seguir puliendo algunas cosas del
sitio, ¿qué cosas?, para empezar, reemplazar el contenido que viene por default
(esos enlaces en el `header` o en el `footer`), agregar algunas páginas y
secciones como un `about`, configurar algunas cositas para que el contenido se
organice por año, que los archivos que se tengan que eliminar se eliminen para
que no haya contenido extraño, etc, etc.

Cómo podemos ver aún hay otros detallitos que iremos revisando pero por ahora ya
podemos tener el sitio andando y con algo de contenido, así que vamos a seguir
con otras cosas y nos leemos pronto.

[See you in space cowboy ...](https://www.youtube.com/watch?v=NRI_8PUXx2A)
