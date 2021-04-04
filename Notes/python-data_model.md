https://docs.python.org/3/reference/datamodel.html?highlight=data%20model

# Basic customization





# with statement
object.__enter__(self)

object.__exit__(self, exc_type, exc_value, traceback)


# 比较
object.__lt__(self, other) # less than
object.__le__(self, other) # less equal
object.__eq__(self, other) # equal
object.__ne__(self, other) # not equal
object.__gt__(self, other) # greater than
object.__ge__(self, other) # greater equal

object.__bool__(self)
object.__hash__(self)

object.__getattr__(self, name)
object.__getattribute__(self, name)

object.__setattr__(self, name, value)
object.__delattr__(self, name)
object.__dir__(self)


object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)

These methods are called to implement the binary arithmetic operations (+, -, * , @, /, //, %, divmod(), pow(), ** , <<, >>, &, ^, |). 

object.__radd__(self, other)
object.__rsub__(self, other)
object.__rmul__(self, other)
object.__rmatmul__(self, other)
object.__rtruediv__(self, other)
object.__rfloordiv__(self, other)
object.__rmod__(self, other)
object.__rdivmod__(self, other)
object.__rpow__(self, other)
object.__rlshift__(self, other)
object.__rrshift__(self, other)
object.__rand__(self, other)
object.__rxor__(self, other)
object.__ror__(self, other)
These methods are called to implement the binary arithmetic operations (+, -, * , @, /, //, %, divmod(), pow(), ** , <<, >>, &, ^, |) with reflected (swapped) operands. These functions are only called if the left operand does not support the corresponding operation [3] and the operands are of different types. [4] For instance, to evaluate the expression x - y, where y is an instance of a class that has an __rsub__() method, y.__rsub__(x) is called if x.__sub__(y) returns NotImplemented.


object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__imatmul__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)
These methods are called to implement the augmented arithmetic assignments (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=). These methods should attempt to do the operation in-place (modifying self) and return the result (which could be, but does not have to be, self). If a specific method is not defined, the augmented assignment falls back to the normal methods. For instance, if x is an instance of a class with an __iadd__() method, x += y is equivalent to x = x.__iadd__(y) . Otherwise, x.__add__(y) and y.__radd__(x) are considered, as with the evaluation of x + y. In certain situations, augmented assignment can result in unexpected errors (see Why does a_tuple[i] += [‘item’] raise an exception when the addition works?), but this behavior is in fact part of the data model.