# cheat
```py
def addMethod(self):
	return True

Class.addMethod = addMethod

# for variable input types.MethodType( barFighters, a )

```


n Python, there is a difference between functions and bound methods.

>>> def foo():
...     print "foo"
...
>>> class A:
...     def bar( self ):
...         print "bar"
...
>>> a = A()
>>> foo
<function foo at 0x00A98D70>
>>> a.bar
<bound method A.bar of <__main__.A instance at 0x00A9BC88>>
>>>
Bound methods have been "bound" (how descriptive) to an instance, and that instance will be passed as the first argument whenever the method is called.

Callables that are attributes of a class (as opposed to an instance) are still unbound, though, so you can modify the class definition whenever you want:

>>> def fooFighters( self ):
...     print "fooFighters"
...
>>> A.fooFighters = fooFighters
>>> a2 = A()
>>> a2.fooFighters
<bound method A.fooFighters of <__main__.A instance at 0x00A9BEB8>>
>>> a2.fooFighters()
fooFighters
Previously defined instances are updated as well (as long as they haven't overridden the attribute themselves):

>>> a.fooFighters()
fooFighters
The problem comes when you want to attach a method to a single instance:

>>> def barFighters( self ):
...     print "barFighters"
...
>>> a.barFighters = barFighters
>>> a.barFighters()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: barFighters() takes exactly 1 argument (0 given)
The function is not automatically bound when it's attached directly to an instance:

>>> a.barFighters
<function barFighters at 0x00A98EF0>
To bind it, we can use the MethodType function in the types module:

>>> import types
>>> a.barFighters = types.MethodType( barFighters, a )
>>> a.barFighters
<bound method ?.barFighters of <__main__.A instance at 0x00A9BC88>>
>>> a.barFighters()
barFighters
This time other instances of the class have not been affected:

>>> a2.barFighters()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: A instance has no attribute 'barFighters'
More information can be found by reading about descriptors and metaclass programming.