ast.parse()

NodeVistor()



```python
from ast import NodeVisitor

class CallVisitor(NodeVisitor):
    def visit_Call(self,node):
        print("saw call to ",node.func.attr," with args ", [i.n for i in node.args])
        return super().generic_visit(node)

def f(x):
    return random.randint(1,100)

from ast import parse
from inspect import getsource

# only for it can access the  corrent source format
#     def...
# not actuall call it
CallVisitor().visit(parse(getsource(f)))



```