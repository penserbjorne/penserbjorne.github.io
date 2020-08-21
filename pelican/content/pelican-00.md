---
Title: Pelican (00), cheat sheet
Date: 2020-08-20
Modified: 2020-08-21
Tags: blog, pelican, cheat sheet
Keywords: blog, pelican, cheat sheet
Category: pelican
Author: Penserbjorne
Summary: Recopilación de comandos para no olvidar como gestionar el blog con Pelican
Lang: es-MX
Translation: false
Status: published
---

# What is this?

Weno weno, ¿de que va esta entrada? Pues simplemente es mi `cheat sheet` para
gestionar este blog con `Pelican`.

Como ya hemos dicho, toda la documentación necesaria (y extendida) se
encuentra en [el blog oficial de Pelican](https://docs.getpelican.com), por lo
que si se necesita mayor información o detalle de algo, visitar el sitio oficial
(recuerda siempre, **\#RTFM**).

# Comandos

## Preparación del entorno

```bash
# Creación del entorno
virtualenv ~/path/to/project

# Nos movemos a la carpeta creada
cd ~/path/to/project

# Activamos el entorno
source bin/activate

# Instalación de herramientas
pip install pelican Markdown typogrify invoke livereload

# Actualización de herramientas
pip install --upgrade pelican Markdown typogrify invoke livereload

# Clonamos repositorio
git clone https://github.com/penserbjorne/penserbjorne.github.io.git
```

## Generar y ejecutar sitio

```bash
# Nos movemos a la carpeta con la fuente del sitio
# Recuerda que ya estabamos dentro dentro de la carpeta del entorno virtual
cd penserbjorne.github.io/pelican

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
