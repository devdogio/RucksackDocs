# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os
import sys

import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
    'doc_extensions',
]
templates_path = ['_templates']

source_suffix = ['.md']
source_parsers = {
    '.md': CommonMarkParser,
}

master_doc = 'README'
project = u'Rucksack docs'
copyright = '2018-{}, Devdog, Inc & contributors'.format(
    timezone.now().year
)
version = '1.0'
release = '1.0'
exclude_patterns = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'
intersphinx_mapping = {
    'python': ('http://python.readthedocs.io/en/latest/', None),
    'sphinx': ('http://sphinx.readthedocs.io/en/latest/', None),
}

htmlhelp_basename = 'RucksackDocs'
exclude_patterns = [
    # 'api' # needed for ``make gettext`` to not die.
]

language = 'en'

locale_dirs = [
    'locale/',
]
gettext_compact = False

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = 'Assets/Logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}

# def setup(app):
    # app.add_stylesheet('custom.css')