# control flow statements
```dart
For loops
You can iterate with the standard for loop. For example:

var message = StringBuffer('Dart is fun');
for (var i = 0; i < 5; i++) {
  message.write('!');
}
Closures inside of Dart’s for loops capture the value of the index, avoiding a common pitfall found in JavaScript. For example, consider:

var callbacks = [];
for (var i = 0; i < 2; i++) {
  callbacks.add(() => print(i));
}
callbacks.forEach((c) => c());
The output is 0 and then 1, as expected. In contrast, the example would print 2 and then 2 in JavaScript.

If the object that you are iterating over is an Iterable, you can use the forEach() method. Using forEach() is a good option if you don’t need to know the current iteration counter:

candidates.forEach((candidate) => candidate.interview());

```

```dart
if (isRaining()) {
  you.bringRainCoat();
} else if (isSnowing()) {
  you.wearJacket();
} else {
  car.putTopDown();
}
```

```dart
While and do-while
A while loop evaluates the condition before the loop:

while (!isDone()) {
  doSomething();
}
A do-while loop evaluates the condition after the loop:

do {
  printLine();
} while (!atEndOfPage());
```

break and contionue

```dart
var command = 'OPEN';
switch (command) {
  case 'CLOSED':
    executeClosed();
    break;
  case 'PENDING':
    executePending();
    break;
  case 'APPROVED':
    executeApproved();
    break;
  case 'DENIED':
    executeDenied();
    break;
  case 'OPEN':
    executeOpen();
    break;
  default:
    executeUnknown();
}
```



# cascade notiation
```dart
class
	..method1
	..method2
```

# A basic Dart program
The following code uses many of Dart’s most basic features:
```dart
// Define a function.
printInteger(int aNumber) {
  print('The number is $aNumber.'); // Print to console.
}

// This is where the app starts executing.
main() {
  var number = 42; // Declare and initialize a variable.
  printInteger(number); // Call a function.
}
```

# Important concepts

# collection if and for
Dart 2.3 also introduced collection if and collection for, which you can use to build collections using conditionals (if) and repetition (for).

Here’s an example of using collection if to create a list with three or four items in it:

var nav = [
  'Home',
  'Furniture',
  'Plants',
  if (promoActive) 'Outlet'
];
Here’s an example of using collection for to manipulate the items of a list before adding them to another list:

var listOfInts = [1, 2, 3];
var listOfStrings = [
  '#0',
  for (var i in listOfInts) '#$i'
];
assert(listOfStrings[1] == '#1');
For more details and examples of using collection if and for, see the control flow collections proposal.

The List type has many handy methods for manipulating lists. For more information about lists, see Generics and Collections.



dart是值传递。我们每次调用函数，传递过去的都是对象的内存地址，而不是这个对象的复制.

直接赋值的1,之类的常量不算.