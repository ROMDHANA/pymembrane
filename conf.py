# Configuration file for the Sphinx documentation builder.

import os
import sys

# Ajouter le chemin de votre module pour que Sphinx le trouve
sys.path.insert(0, os.path.abspath('../pymembrane'))

# Project information
project = 'pymembrane'
copyright = '2024, Hedi Romdhana'
author = 'Hedi Romdhana'

# Extensions nécessaires pour Sphinx
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # Support pour les docstrings Google et NumPy
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',  # Pour marquer les TODOs
    'sphinx.ext.coverage',  # Pour vérifier la couverture des docs
]

# Chemins des modèles Sphinx
templates_path = ['_templates']
exclude_patterns = []

# Thème HTML
html_theme = 'alabaster'
html_static_path = ['_static']

# Déterminer le répertoire actuel
this_directory = os.path.abspath(os.path.dirname(__file__))

# Obtenir la version du projet
version_path = os.path.join(this_directory, '..', 'pymembrane', '__version__.py')
with open(version_path) as f:
    exec(f.read())

# Utiliser la version actuelle comme valeur de `release`
release = __version__
