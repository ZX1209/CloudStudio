https://dart.dev/codelabs/dart-cheatsheet

## string interpolation,字符串插值

String	 	Result
'${3 + 2}'	 	'5'
'${"word".toUpperCase()}'	 	'WORD'
'$myObject'	 	The value of myObject.toString()


## Collection literals,集合迭代
Dart has built-in support for lists, maps, and sets. You can create them using literals:

var aListOfStrings = ['one', 'two', 'three'];
var aSetOfStrings = {'one', 'two', 'three'};
var aMapOfStringsToInts = {
  'one': 1,
  'two': 2,
  'three': 3,
};


Dart’s type inference can assign types to these variables for you. In this case, the inferred types are List<String>, Set<String>, and Map<String, int>.

Or you can specify the type yourself:

var aListOfInts = <int>[];
var aSetOfInts = <int>{};
var aMapOfIntToDouble = <int, double>{};

## Optional positional parameters,可选位置参数
int sumUpToFive(int a, [int b, int c, int d, int e]) {
  int sum = a;
  if (b != null) sum += b;
  if (c != null) sum += c;
  if (d != null) sum += d;
  if (e != null) sum += e;
  return sum;
}
// ···
  int total = sumUpToFive(1, 2);
  int otherTotal = sumUpToFive(1, 2, 3, 4, 5);


Optional positional parameters are always last in a function’s parameter list. Their default value is null unless you provide another default value:

int sumUpToFive(int a, [int b = 2, int c = 3, int d = 4, int e = 5]) {
// ···
}
// ···
  int newTotal = sumUpToFive(1);
  print(newTotal); // <-- prints 15

## Optional named parameters,可选命名参数
Using a curly brace syntax, you can define optional parameters that have names.

void printName(String firstName, String lastName, {String suffix}) {
  print('$firstName $lastName ${suffix ?? ''}');
}
// ···
  printName('Avinash', 'Gupta');
  printName('Poshmeister', 'Moneybuckets', suffix: 'IV');
As you might expect, the value of these parameters is null by default, but you can provide default values:

void printName(String firstName, String lastName, {String suffix = ''}) {
  print('$firstName $lastName $suffix');
}
A function can’t have both optional positional and optional named parameters.

## Cascades,级联

querySelector('#confirm')
..text = 'Confirm'
..classes.add('important')
..onClick.listen((e) => window.alert('Confirmed!'));

equals

var button = querySelector('#confirm');
button.text = 'Confirm';
button.classes.add('important');
button.onClick.listen((e) => window.alert('Confirmed!'));
With cascades, the code becomes much shorter, and you don’t need the button variable:


## Getters and setters,获取和设置方法
You can define getters and setters whenever you need more control over a property than a simple field allows.

For example, you can make sure a property’s value is valid:

class MyClass {
  int _aProperty = 0;

  int get aProperty => _aProperty;

  set aProperty(int value) {
    if (value >= 0) {
      _aProperty = value;
    }
  }
}

## Null-aware operators,空感知运算符
int a; // The initial value of a is null.
a ??= 3;
print(a); // <-- Prints 3.

a ??= 5;
print(a); // <-- Still prints 3.

print(1 ?? 3); // <-- Prints 1.
print(null ?? 12); // <-- Prints 12.

## Conditional property access,条件方法使用
To guard access to a property or method of an object that might be null, put a question mark (?) before the dot (.):

myObject?.someProperty
The preceding code is equivalent to the following:

(myObject != null) ? myObject.someProperty : null



## Arrow syntax,箭头语法
bool hasEmpty = aListOfStrings.any((s) => s.isEmpty);\






## exception, 异常
try {
  breedMoreLlamas();
} catch (e) {
  // ... handle exception ...
} finally {
  // Always clean up, even if an exception is thrown.
  cleanLlamaStalls();
}

## Using this in a constructor
Dart provides a handy shortcut for assigning values to properties in a constructor: use this.propertyName when declaring the constructor:

class MyColor {
  int red;
  int green;
  int blue;

  MyColor(this.red, this.green, this.blue);
}

final color = MyColor(80, 80, 128);


## Initializer lists
Sometimes when you implement a constructor, you need to do some setup before the constructor body executes. For example, final fields must have values before the constructor body executes. Do this work in an initializer list, which goes between the constructor’s signature and its body:

Point.fromJson(Map<String, num> json)
    : x = json['x'],
      y = json['y'] {
  print('In Point.fromJson(): ($x, $y)');
}
The initializer list is also a handy place to put asserts, which run only during development:

NonNegativePoint(this.x, this.y)
    : assert(x >= 0),
      assert(y >= 0) {
  print('I just made a NonNegativePoint: ($x, $y)');
}


## Named constructors,命名构造器
To allow classes to have multiple constructors, Dart supports named constructors:

class Point {
  double x, y;

  Point(this.x, this.y);

  Point.origin() {
    x = 0;
    y = 0;
  }
}
To use a named constructor, invoke it using its full name:

final myPoint = Point.origin();

## factory constructors,
...
## Redirecting constructors,重定向构造器
Sometimes a constructor’s only purpose is to redirect to another constructor in the same class. A redirecting constructor’s body is empty, with the constructor call appearing after a colon (:).

class Automobile {
  String make;
  String model;
  int mpg;

  // The main constructor for this class.
  Automobile(this.make, this.model, this.mpg);

  // Delegates to the main constructor.
  Automobile.hybrid(String make, String model) : this(make, model, 60);

  // Delegates to a named constructor
  Automobile.fancyHybrid() : this.hybrid('Futurecar', 'Mark 2');
}

## Const constructors,固定构造函数
If your class produces objects that never change, you can make these objects compile-time constants. To do this, define a const constructor and make sure that all instance variables are final.

class ImmutablePoint {
  const ImmutablePoint(this.x, this.y);

  final int x;
  final int y;

  static const ImmutablePoint origin = ImmutablePoint(0, 0);
}

