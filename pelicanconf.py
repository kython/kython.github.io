#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kython'
SITENAME = u'Kython Liao'
TAGLINE = 'PHD-Candidate.<br> Enjoy Python & Mathematica.<br> Living in Shanghai.'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['blog', 'images', 'pdfs']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
TEMPLATE_PAGES = {'pages/marryu.html': 'pages/marryu.html'}

SUMMARY_MAX_LENGTH = 50

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Theme and theme settings
THEME = 'themes/kythonboot'
COVER_IMG_URL = 'http://upload.jianshu.io/daily_images/images/BKx3sA9CumMFpUzQJTFx.jpg'
PROFILE_IMAGE_URL = 'https://avatars2.githubusercontent.com/u/7881268?v=3&s=460'
MENUITEMS = (('Home','index.html'), ('About','pages/about-me.html'), ('Moments','pages/marryu.html'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/kython'),
          ('weibo', 'http://weibo.com/abcy618'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
