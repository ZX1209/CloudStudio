Installation
This package runs under Python 2.7, and 3.5+, use pip to install:

$ pip install graphviz
To render the generated DOT source code, you also need to install Graphviz (download page).

Make sure that the directory containing the dot executable is on your systems’ path.

# Quickstart
## Create a graph object:

>>> from graphviz import Digraph

>>> dot = Digraph(comment='The Round Table')

>>> dot  #doctest: +ELLIPSIS
<graphviz.dot.Digraph object at 0x...>
## Add nodes and edges:

>>> dot.node('A', 'King Arthur')
>>> dot.node('B', 'Sir Bedevere the Wise')
>>> dot.node('L', 'Sir Lancelot the Brave')

>>> dot.edges(['AB', 'AL'])
>>> dot.edge('B', 'L', constraint='false')
## Check the generated source code:

>>> print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
// The Round Table
digraph {
    A [label="King Arthur"]
    B [label="Sir Bedevere the Wise"]
    L [label="Sir Lancelot the Brave"]
    A -> B
    A -> L
    B -> L [constraint=false]
}
## Save and render the source code, optionally view the result:

>>> dot.render('test-output/round-table.gv', view=True)  # doctest: +SKIP
'test-output/round-table.gv.pdf'
https://raw.github.com/xflr6/graphviz/master/docs/round-table.png
See also
pygraphviz – full-blown interface wrapping the Graphviz C library with SWIG
graphviz-python – official Python bindings (documentation)
pydot – stable pure-Python approach, requires pyparsing
License
This package is distributed under the MIT license.