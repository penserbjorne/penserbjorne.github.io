#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Penserbjorne'
SITENAME = u'Blog de Penserbjorne'
SITESUBTITLE = u'Otro sitio clíche de tecnología (que no sabe utilizar acentos) >;v'
#SITEURL = 'https://penserbjorne.com'

PATH = 'content'
OUTPUT_PATH = './../'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = u'es'

THEME = u'bootstrap2-dark'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Some liks
GITHUB_URL = 'https://github.com/penserbjorne/'
TWITTER_USERNAME = '@_penserbjorne'

# Blogroll
LINKS = (
            ('LIDSoL', 'https://lidsol.org/'),
            ('Comunidad Elotl', 'https://elotl.mx/'),
            ('protege.la', 'https://protege.la/'),
            ('SocialTIC', 'https://socialtic.org/'),
        )

# Social widget
SOCIAL = (
            ('twitter', 'https://twitter.com/_penserbjorne'),
            ('github', 'https://github.com/penserbjorne/'),
         )

DEFAULT_PAGINATION = 10

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
