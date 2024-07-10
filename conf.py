import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'ICICLE Training Catalog'
author = 'David Lee'
release = '0.1'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output options
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
