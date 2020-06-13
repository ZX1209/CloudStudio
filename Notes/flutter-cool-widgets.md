# PageView
```dart
class PageViewPlay extends StatelessWidget {
  const PageViewPlay({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final controller = PageController(
      initialPage: 1,
    );
    final pageView = PageView(
      scrollDirection: Axis.horizontal,
      controller: controller,
      children: [
        blueBox(),
        redBox(),
        greenBox(),
      ],
    );

    return MaterialApp(
      home: pageView,
    );
  }
}


```

# ExpansionPanel,List,Tile
可伸缩的项

# tabbarview tab页面

# Animation...

# valueListenableBuilder