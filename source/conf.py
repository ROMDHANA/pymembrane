# -*- coding: utf-8 -*-
"""
Configuration file for the Sphinx documentation builder.
"""

import os  # Import os before using it
import sys  # Import sys before using it

# Define the path to your project
sys.path.insert(0, os.path.abspath('../pymembrane'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

# Log the paths being included
print("Python sys.path:", sys.path)

# Check if the 'pymembrane' directory exists
pymembrane_path = os.path.abspath('../pymembrane')
if os.path.exists(pymembrane_path):
    print(f"Directory found: {pymembrane_path}")
    print("Contents:", os.listdir(pymembrane_path))
else:
    print(f"Directory not found: {pymembrane_path}")

# Project information
project = 'pymembrane'
copyright = '2024, Hedi Romdhana'
author = 'Hedi Romdhana'

# Read version directly from pymembrane/__version__.py
version_path = os.path.join(os.path.dirname(__file__), '..', 'pymembrane', '__version__.py')
with open(version_path) as f:
    exec(f.read())  # This defines the variable __version__

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

# Enable Python code execution
ipython_warning = False

# Set the HTML theme
html_theme = "sphinx_book_theme"

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

import doctest
doctest_test_doctest_blocks = 'true'
doctest_default_flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE

# Add JavaScript for "Copy" button
html_js_files = [
    'copy_button.js',
]

# Mock dependencies that might not be present in the build environment
autodoc_mock_imports = ["matplotlib", "numpy", "pandas", "IPython", "cryptography"]

import matplotlib
matplotlib.use('Agg')

plot_html_show_source_link = False
