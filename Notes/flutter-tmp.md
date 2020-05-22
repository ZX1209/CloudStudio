## 1 routes
MaterialApp(
      title: 'Flutter Demo',
      initialRoute: '/items',
      routes: {
        '/items': (context) => FutureItemsW(),
        '/historys': (context) => FutureHistorysW(),
      },
    );

## 2 navigator to
Navigator.pushNamed(context, '/historys', arguments: [this.iid, this.title]);

## 3 get arguments
List<String> args = ModalRoute.of(context).settings.arguments;


## dynamic generate route
onGenerateRoute: (settings) {
    // If you push the PassArguments route
    if (settings.name == PassArgumentsScreen.routeName) {
      // Cast the arguments to the correct type: ScreenArguments.
      final ScreenArguments args = settings.arguments;

      // Then, extract the required data from the arguments and
      // pass the data to the correct screen.
      return MaterialPageRoute(
        builder: (context) {
          return PassArgumentsScreen(
            title: args.title,
            message: args.message,
          );
        },
      );
    }
  },


  ## dialog and flush
  Future<String> _asyncInputDialog(BuildContext context) async {
  String teamName = '';
  return showDialog<String>(
    context: context,
    barrierDismissible: true, // dialog is dismissible with a tap on the barrier
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text('Enter current team'),
        content: new Row(
          children: <Widget>[
            new Expanded(
                child: new TextField(
              autofocus: true,
              decoration: new InputDecoration(labelText: 'item title', hintText: ''),
              onChanged: (value) {
                teamName = value;
              },
            ))
          ],
        ),
        actions: <Widget>[
          FlatButton(
            child: Text('Ok'),
            onPressed: () {
              print(teamName);
              add_item(teamName);

              // exit input and previous item list...
              Navigator.of(context).pop();
              Navigator.of(context).pop();

              Navigator.of(context).pushNamed('/items');
            },
          ),
        ],
      );
    },
  );
}