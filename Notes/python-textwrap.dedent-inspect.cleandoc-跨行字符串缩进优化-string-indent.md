From what I see, a better answer here might be inspect.cleandoc, which does much of what textwrap.dedent does but also fixes the problems that textwrap.dedent has with the leading line.

The below example shows the differences:

>>> import textwrap
>>> import inspect
>>> x = """foo bar
    baz
    foobar
    foobaz
    """
>>> inspect.cleandoc(x)
'foo bar\nbaz\nfoobar\nfoobaz'
>>> textwrap.dedent(x)
'foo bar\n    baz\n    foobar\n    foobaz\n'
>>> y = """
...     foo
...     bar
... """
>>> textwrap.dedent(y)
'\nfoo\nbar\n'
>>> inspect.cleandoc(y)
'foo\nbar'
>>> z = """\tfoo
bar\tbaz
"""
>>> textwrap.dedent(z)
'\tfoo\nbar\tbaz\n'
>>> inspect.cleandoc(z)
'foo\nbar     baz'
Note that inspect.cleandoc also expands internal tabs to spaces. This may be inappropriate for one's use case, but works fine for me.