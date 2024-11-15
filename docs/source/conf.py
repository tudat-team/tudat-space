#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tudat.space documentation build configuration file, created by
# sphinx-quickstart on Sat Jul 18 15:13:31 2020.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
from datetime import datetime


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    # "sphinx.ext.autosectionlabel",
    "sphinx_design",  # for gridded panels, tabs, dropdowns
    "nbsphinx",  # to embed Jupyter notebooks
    "IPython.sphinxext.ipython_console_highlighting",  # to have pygments in rendered notebooks
    "sphinx_copybutton",  # copy button in code blocks
    "sphinx_codeautolink",  # automatically link to API reference in code snippets and examples
]

# Specifying thumbnails according to images in _static folder
nbsphinx_thumbnails = {
    "_src_getting_started/_src_examples/propagation": "./_static/propagation_example_thumbnail.png",
    "_src_getting_started/_src_examples/pygmo": "./_static/pygmo_example_thumbnail.png",
    "_src_getting_started/_src_examples/estimation": "./_static/estimation_example_thumbnail.png",
    "_src_getting_started/_src_examples/mission_design": "./_static/mission_design_example_thumbnail.png",
    "_src_getting_started/_src_examples/pygmo/asteroid_orbit_optimization": "./_static/asteroid_example_thumbnail.png",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Prolog/epilog to Jupyter notebooks

nbsphinx_prolog = """
.. note::
    Generated by nbsphinx_ from a Jupyter_ notebook. All the examples as Jupyter notebooks are available in the 
    tudatpy-examples repo_.
    
    .. _nbsphinx: https://nbsphinx.readthedocs.io/
    .. _Jupyter: https://jupyter.org/
    .. _repo: https://github.com/tudat-team/tudatpy-examples
"""
# This option prevents from re-executing the notebooks. The content stored from the latest execution will be displayed.
nbsphinx_execute = "never"
# The suffix(es) of source filenames.
source_suffix = {".rst": "restructuredtext"}

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "tudat.space"
year = datetime.now().year
copyright = f"{year}, Tudat Team"
author = "Tudat Team"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "0.8"
# The full version, including alpha/beta/rc tags.
release = "0.8.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "navigation_depth": 6,
    "use_edit_page_button": True,
    "pygments_dark_style": "github-dark-high-contrast",
    "pygments_light_style": "github-light-high-contrast",
    "logo": {
        "image_light": "_static/cover.png",
        "image_dark": "_static/cover_dark.png",
    },
    "announcement": "Have thoughts or feedback on the new layout? Let us know in our <a href='https://github.com/orgs/tudat-team/discussions'>Github Discussion forum!</a>",
}

html_context = {
    "github_user": "tudat-team",
    "github_repo": "tudat-space",
    "github_version": "develop",
    "doc_path": "docs/source",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "custom.css" will overwrite the builtin "custom.css".
html_static_path = ["_static"]

# Load stylesheet to set maximum width in html pages
html_css_files = [
    "custom.css",
]

html_favicon = "_static/cover_crop.png"

html_sidebars = {"**": ["sidebar-nav-bs", "sidebar-ethical-ads"]}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "tudatspacedoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "tudatspace.tex", "tudat.space Documentation", "ggarrett13", "manual"),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "tudatspace", "tudat.space Documentation", [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "tudatspace",
        "tudat.space Documentation",
        author,
        "tudatspace",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Example configuration for intersphinx: refer to the Python standard library.
# test / view content of inventory file at url via $ python -msphinx.ext.intersphinx <url>
intersphinx_mapping = {
    "tudatpy": ("https://py.api.tudat.space/en/latest/", None),
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

intersphinx_disabled_reftypes = []

# -- Options for sphinx_codeautolink -------------------------------------------
codeautolink_concat_default = True
