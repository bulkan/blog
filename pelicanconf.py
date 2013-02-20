#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'bulkan'
SITENAME = u'Bulkan Savun Evcimen'
#SITEURL = 'http://ec2-23-20-13-253.compute-1.amazonaws.com'

SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

CSS_FILE = 'stylesheet.css'

# Blogroll
LINKS = (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
         ('Python.org', 'http://python.org'),
         ('Jinja2', 'http://jinja.pocoo.org'),
         ('You can modify those links in your config file', '#'),)


TEMPLATE_PAGES = {'music.html': 'music.html'}

THEME = 'cielo'

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

TWITTER_USERNAME = 'bulkanevcimen'

DEFAULT_PAGINATION = 3
