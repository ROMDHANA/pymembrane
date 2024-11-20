# -*- coding: utf-8 -*-
"""
Configuration file for the Sphinx documentation builder.
"""
import os
import sys

# Assurez-vous que les chemins locaux ne perturbent pas l'import du module installé
sys.path.insert(0, os.path.abspath('.'))

# Mock des dépendances non essentielles pour éviter des erreurs si elles ne sont pas installées
#autodoc_mock_imports = ["matplotlib", "numpy", "pandas", "IPython", "cryptography", "scipy"]
autodoc_mock_imports = []  # Tous les modules nécessaires sont installés


# Informations sur le projet
project = 'pymembrane'
copyright = '2024, Hedi Romdhana'
author = 'Hedi Romdhana'

# Lire la version directement depuis pymembrane.__version__
try:
    from pymembrane import __version__
    release = __version__.__version__
except ImportError:
    release = "0.0.4"  # Version par défaut si pymembrane n'est pas accessible

# Extensions Sphinx
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

# Configuration des chemins de templates et fichiers statiques
templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = []

# Configurer les paramètres de Napoleon pour les docstrings Google ou NumPy
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# Générer automatiquement des tableaux de résumé pour les classes et fonctions documentées
autosummary_generate = True

# Configurer le thème HTML
html_theme = "sphinx_book_theme"
html_css_files = [
    'custom.css',  # Si un fichier CSS personnalisé existe
]
html_js_files = [
    'copy_button.js',  # Si un fichier JS personnalisé existe
]

# Configuration Matplotlib pour les environnements sans interface graphique
import matplotlib
matplotlib.use('Agg')
plot_html_show_source_link = False

# Doctest pour exécuter des blocs de code dans les docstrings
import doctest
doctest_test_doctest_blocks = 'true'
doctest_default_flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE

# Personnalisation des rôles avec docutils
from docutils import nodes
from docutils.parsers.rst import roles

def type_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """Custom role to style the type with a specific CSS class."""
    options = options or {}
    content = content or []
    node = nodes.inline(rawtext, text, classes=['type-badge'])
    return [node], []

roles.register_local_role('type', type_role)

version_badge_url = f"https://img.shields.io/badge/version-{release}-blue.svg"

rst_prolog = f"""
.. |version_badge| image:: {version_badge_url}
   :alt: Version Badge
"""
email = "hedi.romdhana@agroparistech.fr"
author = "Hedi Romdhana"
