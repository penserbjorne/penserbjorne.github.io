---
Title: Pelican (04), configuración del sitio (tema)
Date: 2020-08-21
Modified: 2020-04-04
Tags: blog, pelican
Keywords: blog, pelican
Category: pelican
Author: Penserbjorne
Summary: Configuración para añadir un tema a un sitio con Pelican
Lang: es-MX
Translation: false
Status: published
---

##  What is this?

Andamos con todo, anoche terminamos la
[tercera entrada de Pelican]({filename}./pelican-03.md) para modificar la
construcción del sitio y configurar algunas cositas del sitio, sé que no es
mucho, pero es trabajo honesto haha

Bueno, esta cuarta entrada será para configurar un tema a nuestro sitio.

Y el *disclaimer* de siempre, como ya hemos dicho, toda la documentación necesaria
(y extendida) se encuentra en [el blog oficial de Pelican](https://docs.getpelican.com),
por lo que si se necesita mayor información o detalle de algo, visitar el sitio
oficial.

##  pelican-themes

Dentro de las herramientas que necesitamos utilizar con `Pelican` se encuentra
`pelican-themes` la cual como su nombre lo indica es para trabajar con temas :\'v

Esta herramientas nos va a permitir gestionar temas pudiendo instalarlos en
nuestro equipo para utilizarlos al desarrollar el sitio, así como eliminarlos.

Esta herramienta ya viene instalada junto con `Pelican` asi que no necesitamos
realizar pasos extras.

Los parámetros que toma la herramienta son los siguientes:

```bash
-l, --list
  Show the themes already installed

-i theme_path, --install theme_path
  One or more themes to install

-r theme_name, --remove theme_name
  One or more themes to remove

-s theme_path, --symlink theme_path
  Same as “–install”, but create a symbolic link instead of copying the theme.
  Useful for theme development

-v, --verbose
  Verbose output
```

Si quieres ver algunos ejemplos de uso más detallados puedes revisar la sección
correspondiente de la documentación de `Pelican` dando click
[aquí](https://docs.getpelican.com/en/stable/pelican-themes.html).

##  Seleccionando e instalando un tema

Vale, ya vimos que podemos *instalar* temas y utilizarlos, pero, ¿donde están
los temas? Tranqui, para eso, `Pelican` tiene un listado de temas en `GitHub`
que puedes revisar entrando
[aquí](https://github.com/getpelican/pelican-themes).

Ahí mismo en el `GitHub` podrás encontrar otra forma de trabajar con temas por
si la que vemos aquí no te agrada.

Para utilizar un tema primero necesitamos clonar el repositorio de temas de
`Pelican`. Este repositorio no tiene que estar dentro de tu repositorio actual
del blog, así que guardalo en otra ubicación..

Para descargarlo utilizaremos el parámetro  `--recursive` para clonar el repo
junto a sus submodulos, y a los submodulos de los submodulos, y así
recursivamente xD. Esto es básicamente para que los temas no se rompan al
clonarlos por falta de algún submodulo.

```bash
git clone --recursive https://github.com/getpelican/pelican-themes ~/path-to-projects/pelican-themes
```

Ya tenemos clonados los temas en nuestro equipo, por lo cual podemos *instalar*
uno el sitio que estamos desarrollando. Para esto le indicaremos a
`pelican-themes` la ruta donde se encuentran los archivos del tema.

Del listado de temas vamos a probar con
[bootstrap2-dark](https://github.com/getpelican/pelican-themes/tree/master/bootstrap2-dark), hemos elegido este tema simplemente porque somos demasiado cliche. La
carpeta donde se encuentran los archivos fuente del tema en este caso es
`~/path-to-projects/pelican-themes/bootstrap2-dark`, y es la que indicaremos a
`pelican-themes`.

```bash
pelican-themes --install ~/path-to-projects/pelican-themes/bootstrap2-dark
```

Si queremos ver cuales temas se encuentran instalados podemos ejecutar:

```bash
pelican-themes --list
```

El cual nos dará una salida como la siguiente:

```bash
notmyidea
bootstrap2-dark
simple
```

En la salida anterior podemos observar que tenemos tres instalados, los dos que
vienen predeterminados en `Pelican` que son `notmyidea` y `simple`, y el que
hemos instalado previamente, `bootstrap2-dark`.

En caso de querer eliminar algún tema instalado podemos ejecutar:

```bash
# Para eliminar un solo tema
pelican-themes --remove nombre-del-tema

# Para eliminar varios temas
pelican-themes --remove nombre-del-tema-1 nombre-del-tema-2 nombre-del-tema-3
```

##  Aplicando el tema instalado

Para poder utilizar nuestro tema instalado tenemos que ir al archivo
`pelicanconf.py` y asignarle un valor a la variable `THEME`, en este caso la
variable quedaría como `THEME = u'bootstrap2-dark'`.

Con este pequeño cambio basta para construir el sitio con el tema seleccionado.
recuerda que utilizaremos los comandos de la [entrada anterior]({filename}./pelican-03.md).

```bash
# Desarrollo
invoke livereload

# Producción
invoke gh-pages
```

Para probar otros temas basta con seguir los pasos anteriores hasta encontrar
uno que sea de tu agrado :)

##  Siguientes pasos (this is (not) the end)

Nuestro sitio ya tiene un poco más de personalidad aunque sigue siendo bastante
cliché, al menos ya es responsivo y se podrá leer en dispositivos móviles.

Para siguientes entradas nos haria falta revisar como agregar algunas secciones
como un `about` o un `contact` y revisar el tema de plugins, y probablemente
con eso habremos terminado de configurar el sitio :)

##  Ejemplos de temas aplicados

Sé que puedes pensar lo siguiente:

>Penserbjorne, pero ... ya termino la entrada, ¿por qué añades otra sección?

Bueno, te quería mostrar algunas imágenes de cómo se ve el tema aplicado al
sitio, solo que las imágenes son muy largas  y por eso decidí dejarlas al final.

Durante el desarrollo de esta entrada utilizamos el tema `bootstrap2-dark`
porqué se vería **chido** pero ya en producción realmente no era muy responsivo
por lo que cambiamos al tema `elegant`.

A continuación te muestro la página de inicio del blog con cada uno de los
temas aplicados.

### Not my idea

Es el tema que trae `Pelican` por defecto, y no, no es responsivo.

![Alt Text]({static}/images/07-pelican-04/screenshot-2020-08-21-blog-de-penserbjorne-1.png)

### bootstrap2-black

Fue el tema **juakeril** que habíamos elegido, pero no, tampoco es responsivo
y después se volvió complicado de leer.

![Alt Text]({static}/images/07-pelican-04/screenshot-2020-08-21-blog-de-penserbjorne-2.png)

### elegant

Es el último tema que hemos probado, sí, es responsivo y es fácil de leer en él,
por lo cual se ha quedado cómo tema final (es el actual a este momento de
  publicación).

![Alt Text]({static}/images/07-pelican-04/screenshot-2021-04-04-blog-de-penserbjorne.png)

##  The End of the Post

Bueno, ahora sí, nos vemos en otra ocasión [piloto](https://www.youtube.com/watch?v=pVeKyqV1jWU).
