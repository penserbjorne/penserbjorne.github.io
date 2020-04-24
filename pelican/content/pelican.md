---
Title: Creación y mantenimiento de un blog estático con Pelican
Date: 2020-04-11
Modified: 2020-04-24
Tags: blog pelican
Keywords: blog pelican
Category: pelican
Author: Penserbjorne
Summary: Creación y mantenimiento de un blog estático con Pelican
Lang: es-MX
Translation: false
Status: draft
---

##

sudo apt install virtualenv

# Creamos el entorno

virtualenv ~/Proyectos/pelican
cd ~/Proyectos/pelican
source bin/activate

# para salir
deactivate

# instalamos pelican
pip install pelican
pip install Markdown
pip install typogrify

# actualizar pelican
pip install --upgrade pelican

# creamos proyecto basado en un esquelo
pelican-quickstart

```
yourproject/
├── content
│   └── (pages)
├── output
├── tasks.py
├── Makefile
├── pelicanconf.py       # Main settings file
└── publishconf.py       # Settings to use when ready to publish
```

# generar el sitio
pelican content

# genera el sitio si esta en una sub carpeta y queremos la salida una carpeta arriba
cd pelican
pelican content -o ..

# preview del sitio
pelican --listen

# con el output modificado
pelican --listen -o ..

http://localhost:8000/

# Contenido

```
Metadata 	Description
title 	Title of the article or page
date 	Publication date (e.g., YYYY-MM-DD HH:SS)
modified 	Modification date (e.g., YYYY-MM-DD HH:SS)
tags 	Content tags, separated by commas
keywords 	Content keywords, separated by commas (HTML content only)
category 	Content category (one only — not multiple)
slug 	Identifier used in URLs and translations
author 	Content author, when there is only one
authors 	Content authors, when there are multiple
summary 	Brief description of content for index pages
lang 	Content language ID (en, fr, etc.)
translation 	Is content is a translation of another (true or false)
status 	Content status: draft, hidden, or published
template 	Name of template to use to generate content (without extension)
save_as 	Save content to this relative file path
url 	URL to use for this article/page
```
