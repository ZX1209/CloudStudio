## build stream
```dart
Stream<int> ints async *{
    for(int i=0;i<10>;i++){
        yield i;
    }
}

```

## reading and decoding a file
```dart
import 'dart:convert';
import 'dart:io';

Future<void> main(List<String> args) async {
  var file = File(args[0]);
  var lines = file
      .openRead()
      .transform(utf8.decoder)
      .transform(LineSplitter());
  await for (var line in lines) {
    if (!line.startsWith('#')) print(line);
  }
}
```

## listen and subscription
```dart 
StreamSubscription<T> listen(void Function(T event) onData,
    {Function onError, void Function() onDone, bool cancelOnError});
```

## broadcast
```dart
final muStream = NumberCreator().stream.asBroadcastStream;

final sub = myStream.listen(print)

final sub2 = myStream.listen(print)

```

## streamcontrol

## erroer handle 
```dart
final sub = myStream.listen(
    (data) {print(data)},
    onError: (err){print(err);},
    cancelOnError: false,
    onDone: print
```
## subsscation metond

## stream control
```dart
class NumberCreator{
    NumberCreator(){
        Timer periodic(Duration(seconds:1),(t){
        _controller.sink.add(_count);
        _count++;
        }

        )
    }
    var _count =1;
    final _controler = StreamController<int>();

    Stream<int> get Stream => _controler.stream;

}


```

## build Future
```dart
Future<int> sumStream(Stream<int> stream) async {
  var sum = 0;
  await for (var value in stream) {
    sum += value;
  }
  return sum;
}
```

## tmp
```dart


```