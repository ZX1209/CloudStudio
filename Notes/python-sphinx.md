toctree 与内容之间要有一个空格

include 写的是相对文件的路径

使用链接来include toctree


source...什么的

.. include:: ../../README.md

rst

##  install
pip install -U sphinx


## extensions 
###   autodoc
pip install -U autodoc

###   autosummary
pip install autodocsumm

extension append
"autodocsumm"


###   recommonmark
markdown

pip install --upgrade recommonmark

extensions = ['recommonmark']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}



###   viewcode
extensions append

"sphinx.ext.viewcode"


##  start
sphinx-quickstart

###   conf.py
```py
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
import os
import sys

sys.path.insert(0, os.path.abspath("./../../"))
sys.path.insert(0, os.path.abspath("./../../test2/"))

import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = "test"
author = "gl"

# The full version, including alpha/beta/rc tags
release = "0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "autodocsumm",
]

autodoc_default_options = {
    "autosummary": True,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
autodata_content = "both"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "classic"
html_theme = "furo"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


```


###   Makefile
```makefile
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

apidoc:
	sphinx-apidoc -o ./source ../ -f
	sphinx-apidoc -o ./source ../test2 -f

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

```

autodoc
autotoc


## 行为指导
###   刷新顺序
make apidoc;make html;

###  添加文件夹
conf.py
sys.path.insert(0, os.path.abspath("./../../test2/"))


make

###   指南?
> https://www.sphinx-doc.org/zh_CN/master/

## za 
toctree 空一行

###   theme
####    furo
1. Install Furo in documentation's build environment.

`pip install furo`


2. Update the html_theme in conf.py.
`html_theme = "furo"`


3. Your Sphinx documentation's HTML pages will now be generated with this theme! 

####    read the docs
This theme is distributed on PyPI and can be installed with pip:

$ pip install sphinx-rtd-theme
To use the theme in your Sphinx project, you will need to add the following to your conf.py file:

import sphinx_rtd_theme

extensions = [
    ...
    "sphinx_rtd_theme",
]

html_theme = "sphinx_rtd_theme"
For more information read the full documentation on installing the theme