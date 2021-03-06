# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

copyright = '2020, SDU eScience'
author = 'DeiC Project 5 Collaboration'
html_title = "Deic Project 5"
# html_logo = ""
# html_favicon = "path/to/favicon.ico"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_comments', 
              'myst_parser', 
              'sphinxcontrib.pdfembed',
              'sphinx_inline_tabs',
              'sphinxcontrib.exceltable',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.mathjax',
              'sphinx.ext.intersphinx',
              'sphinx.ext.extlinks',
              'sphinx.ext.autodoc']

todo_include_todos = True

comments_config = {
    # "hypothesis": True,
    "utterances": {
        "repo": "https://github.com/SDU-eScience/Project5",
        "optional": "config",
    },
    # "dokieli": True
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = ".rst"

master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_book_theme'

# html_theme_options = {
#     "path_to_docs": "docsrc",
#     "repository_branch": "master",
#     "repository_url": "https://github.com/SDU-eScience/Project5",
#     "use_repository_button": True,
#     "use_issues_button": True,
#     "use_edit_page_button": True,
#     "home_page_in_toc": False,
#     "extra_navbar": "", # customize sidebar footer
#     "show_navbar_depth": 2,
# }

html_theme = 'furo'

color1 = "#006aff"
color2 = "#FF9812"

html_theme_options = {
    "light_css_variables": {
        "color-sidebar-background": color1,
        "color-sidebar-brand-text": "white",
        "color-sidebar-caption-text": color2,
        "color-sidebar-item-background--current": "white",
        "color-sidebar-link-text": "white",
        "color-sidebar-link-text--top-level": "white",
        "color-sidebar-background-border": "black",
        "color-sidebar-item-background--current": color1,
        "color-sidebar-item-background--hover": color2,
        "color-sidebar-search-background": "white",
        "color-sidebar-item-expander-background--hover": color1,
        "color-toc-item-text--active": color1,
        "color-brand-content": "white",
        "color-link": color1,
        "color-link--hover": color2,
        "color-link-underline": color1,
        "color-link-underline--hover": color2,
        "font-stack": "Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
        "color-foreground-secondary": color1,
        "color-foreground-muted": color2, # contents
        "color-background-secondary": color1,
        "color-background-border": "black",
        "color-foreground-border": "black"
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}

myst_admonition_enable = True
myst_deflist_enable = True
myst_heading_anchors = 3

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

