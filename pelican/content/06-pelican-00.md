---
Title: Pelican (00), cheat sheet
Date: 2020-08-20
Modified: 2021-04-04
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
que si se necesita mayor información o detalle de algo, visitar el sitio oficial.

# Comandos

##  Preparación del entorno

```bash
# Creación del entorno
virtualenv --python=/usr/bin/python3 ~/path/to/virtual/env

# Nos movemos a la carpeta creada
cd ~/path/to/virtual/env

# Activamos el entorno
source ./bin/activate

# Instalación de herramientas
pip install pelican Markdown typogrify invoke livereload ghp-import

# Actualización de herramientas
pip install --upgrade pelican Markdown typogrify invoke livereload ghp-import

# Clonamos repositorio
git clone https://github.com/penserbjorne/penserbjorne.github.io.git

# Nos movemos a la carpeta con la fuente del sitio
# Recuerda que ya estabamos dentro dentro de la carpeta del entorno virtual
cd penserbjorne.github.io/pelican
```

##  Instalación de un tema

```bash
# Clonar temas
git clone --recursive https://github.com/getpelican/pelican-themes ~/path-to-projects/pelican-themes

# Instalar tema
pelican-themes --install ~/path-to-projects/pelican-themes/bootstrap2-dark

# Listar temas instalados
pelican-themes --list

# Para eliminar un solo tema
pelican-themes --remove nombre-del-tema
```

##  Comando para generar y ejecutar sitio (corta)

Recuerda algunas de estas tareas fueron modificadas para ajustarse al flujo de
de desarrollo del sitio.

```bash
# Desarrollo
invoke livereload

# Producción
invoke gh-pages
```

## Comando para generar y ejecutar sitio (extendida)

Recuerda algunas de estas tareas fueron modificadas para ajustarse al flujo de
de desarrollo del sitio.

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
# y regenerar el sitio cada vez que haya un cambio, todo para local
invoke livereload

# Permite subir el sitio al servidor correspondiente mediante rsync y SSH
invoke publish

# Publica el sitio de producción en Github Pages
invoke gh-pages
```
