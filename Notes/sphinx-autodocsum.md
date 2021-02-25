> https://stackoverflow.com/questions/28307051/automodule-to-generate-toc-in-sphinx-documents

The autodocsumm extension will allow autodoc directives (automodule, autoclass) to automatically add summary tables like those of the builtin autosummary extension.

It can be used as follows:

pip install autodocsumm
Then edit your conf.py to add the extension:

extensions = [
    'sphinx.ext.autodoc',
    ...,
    'autodocsumm',
]
and add an :autosummary: option to your autodoc directives, e.g.:

.. automodule: foo.bar
    :autosummary:
If you want to have autosummary in effect for all your autodoc directives without explicitly adding them, you can do so from the conf.py as follows:

autodoc_default_options = {
    'autosummary': True,
}
This is particularly helpful if you dynamically generate your API pages with sphinx-apidoc which is not easily configurable to add :autosummary:.

Full example of a conf.py that autogenerates all API pages:

def setup(app):
    from sphinx.ext import apidoc
    app.connect('builder-inited', lambda _: apidoc.main([
        '-o', './api', '-d2', '-feMT', '../src/PROJECT',
    ]))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'autodocsumm',
]


autodoc_default_options = {
    'autosummary': True,
}

autodata_content = 'both'