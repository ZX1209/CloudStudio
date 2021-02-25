 
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

// var url = 'https://example.com/whatsit/create';
// var response = await http.post(url, body: {'name': 'doodle', 'color': 'blue'});
// print('Response status: ${response.statusCode}');
// print('Response body: ${response.body}');

// print(await http.read('https://example.com/foobar.txt'));
var base_url = "http://127.0.0.1:8000";

void main() {
  runApp(ToDoApp());
}

class Todos extends StatefulWidget {
  Todos({Key key}) : super(key: key);

  @override
  _TodosState createState() => _TodosState();
}

class _TodosState extends State<Todos> {
  bool isfetched = false;
  var _data = null;
  int _len = 0;

  void get_data() async {
    // Await the http get response, then decode the json-formatted response.
    var response = await http.get(base_url + "/todos" + "?item_id=100");

    if (response.statusCode == 200) {
      isfetched = true;
      _data = convert.jsonDecode(response.body);
      print(_data);

      _len = _data.length;

      print('Number of books about http: $_len.');
    } else {
      print('Request failed with status: ${response.statusCode}.');
    }

    setState(() {});
  }

  @override
  void initState() {
    super.initState();
    get_data();
  }

  @override
  Widget build(BuildContext context) {
    if (isfetched) {
      return ListView.builder(
        itemCount: _len,
        itemBuilder: (BuildContext context, int index) {
          return ListTile(
            title: Text(_data[index]["__data__"]["title"]),
          );
        },
      );
    } else {
      return Text('No data');
    }

    // return FutureBuilder<List>(
    //   future: _todos, // a previously-obtained Future<String> or null
    //   builder: (BuildContext context, AsyncSnapshot<List> snapshot) {
    //     Widget child = null;

    //     if (snapshot.hasData) {
    //       child = ListView(
    //           children: snapshot.data
    //               .map((item) => ListTile(
    //                     title: item["__data__"]["title"],
    //                   ))
    //               .toList());
    //     } else {
    //       child = Text('error');
    //     }
    //     return child;
    //   },
    // );
  }
}

class ToDoApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Material App',
      home: Scaffold(
          appBar: AppBar(
            title: Text('Material App Bar'),
          ),
          body: Todos()),
    );
  }
}
