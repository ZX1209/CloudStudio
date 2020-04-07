```dart
import 'dart:io';
import 'dart:async'

 String dir = (await getApplicationDocumentsDirectory()).path;
    return new File('$dir/counter.txt');

File file = await _getLocalFile();
      // read the variable as a string from the file.
      String contents = await file.readAsString();

```