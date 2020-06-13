## auto refush
Navigator.push(context, MaterialPageRoute(builder: (context) => Page2())).then((value) {
                  setState(() {
                    // refresh state of Page1
                  });
                });


## push pop
// 位于 FirstRoute widget (Within the `FirstRoute` widget)
onPressed: () {
  Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => SecondRoute()),
  );
}

// 位于 SecondRoute widget (Within the SecondRoute widget)
onPressed: () {
  Navigator.pop(context);
}

## pushnamed
接下来，我们需要通过为 MaterialApp 的构造函数额外的属性： initialRoute 和 routes 来定义我们的路由。

initialRoute 属性定义了应用应该从哪个路由启动。 routes 属性定义了所有可用的命名路由，以及当我们跳转到这些路由时应该构建的 widgets。

content_copy
MaterialApp(
  // Start the app with the "/" named route. In this case, the app starts
  // on the FirstScreen widget.
  
  // 使用“/”命名路由来启动应用（Start the app with the "/" named route. In our case, the app will start）
  // 在这里，应用将从 FirstScreen Widget 启动（on the FirstScreen Widget）
  
  initialRoute: '/',
  routes: {
    // When navigating to the "/" route, build the FirstScreen widget.
    // 当我们跳转到“/”时，构建 FirstScreen Widget（When we navigate to the "/" route, build the FirstScreen Widget）
    '/': (context) => FirstScreen(),
    // When navigating to the "/second" route, build the SecondScreen widget.
    // 当我们跳转到“/second”时，构建 SecondScreen Widget（When we navigate to the "/second" route, build the SecondScreen Widget）
    '/second': (context) => SecondScreen(),
  },
);
 请注意

当使用 initialRoute 时，需要确保你没有同时定义 home 属性。

// Within the `FirstScreen` widget
// 在 `FirstScreen` Widget中（Within the `FirstScreen` Widget）
onPressed: () {
  // Navigate to the second screen using a named route.
  // 使用命名路由跳转到第二个界面（Navigate to the second screen using a named route）
  Navigator.pushNamed(context, '/second');
}