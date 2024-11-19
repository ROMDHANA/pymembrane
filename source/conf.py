# -*- coding: utf-8 -*-
"""
Configuration file for the Sphinx documentation builder.
"""

import os
import sys

# Définir le chemin vers le projet
sys.path.insert(0, os.path.abspath('../pymembrane'))

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'pymembrane'
copyright = '2024, Hedi Romdhana'
author = 'Hedi Romdhana'

# Lecture de la version directement à partir de pymembrane/__version__.py
version_path = os.path.join(os.path.dirname(__file__), '..', 'pymembrane', '__version__.py')
with open(version_path) as f:
    exec(f.read())  # Cela définit la variable __version__

release = __version__

# Add Sphinx extensions

extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
]

    # 'sphinx.ext.autosummary',
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.napoleon',
    # 'sphinx.ext.viewcode',
    # 'sphinx.ext.imgmath',  # Pour le rendu des mathématiques
    # 'sphinx.ext.mathjax',  # Pour la gestion des mathématiques
    # 'IPython.sphinxext.ipython_console_highlighting',
    # 'IPython.sphinxext.ipython_directive',
    # 'matplotlib.sphinxext.plot_directive',  # Utiliser l'extension de matplotlib


# Templates and HTML output
templates_path = ['_templates']
exclude_patterns = []

html_static_path = ['_static']
html_css_files = [
    'custom.css',  # Link to your custom CSS file
]

# Napoleon settings for Google-style or NumPy-style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# Automatically generate summary tables for documented classes and functions.
autosummary_generate = True

# Activer l'exécution de code Python
ipython_warning = False

#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
html_theme = "sphinx_book_theme"

# # Options du thème RTD (Read the Docs)
# html_theme_options = {
#      'collapse_navigation': False,  # Ne pas réduire la navigation
#      'sticky_navigation': True,     # Garder la navigation visible
#      'navigation_depth': 4,         # Profondeur de navigation
#      #'display_version': True,       # Afficher la version
#      'style_external_links': True,  # Appliquer des styles spécifiques aux liens externes
# #     'font_family': 'Georgia, serif',  # Famille de police pour le texte principal
# #     'head_font_family': 'Arial, sans-serif',  # Police des titres
# #     'font_size': '16px',  # Taille de police pour le texte principal
# }

from docutils import nodes
from docutils.parsers.rst import roles

def type_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """Custom role to style the type with a specific CSS class."""
    options = options or {}
    content = content or []
    node = nodes.inline(rawtext, text, classes=['type-badge'])
    return [node], []

# Register the role as "type"
roles.register_local_role('type', type_role)

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

import doctest
doctest_test_doctest_blocks = 'true'
doctest_default_flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE

# Add JavaScript for "Copy" button
html_js_files = [
    'copy_button.js',
]

# Mock dependencies that might not be present in the build environment
autodoc_mock_imports = ["matplotlib", "numpy", "pandas", "pymembrane","IPython","cryptography"]



import matplotlib
matplotlib.use('Agg')

plot_html_show_source_link=False




