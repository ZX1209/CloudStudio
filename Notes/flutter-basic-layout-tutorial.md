# Row and Column classes
return Row(
      children: [
        BlueBox(),
        BlueBox(),
        BlueBox(),
      ],)

? children : [] list 直接解析?


# Axis size and alignment

## mainAxisSize property (主轴尺寸)

### MainAxisSize.max
Row and Column occupy all of the space on their main axes. If the combined width of their children is less than the total space on their main axes, their children are laid out with extra space.

### MainAxisSize.min
Row and Column only occupy enough space on their main axes for their children.** Their children are laid out without extra space and at the middle of their main axes. **

## mainAxisAlignment property (主轴对齐方式)
### MainAxisAlignment.start
Positions children near the beginning of the main axis. (Left for Row, top for Column)

### MainAxisAlignment.end
Positions children near the end of the main axis. (Right for Row, bottom for Column)

### MainAxisAlignment.center
Positions children at the middle of the main axis.

### MainAxisAlignment.spaceBetween
Divides the extra space evenly between children.

### MainAxisAlignment.spaceEvenly
Divides the extra space evenly between children and before and after the children.

### MainAxisAlignment.spaceAround
Similar to MainAxisAlignment.spaceEvenly, but reduces half of the space before the first child and after the last child to half of the width between the children.

## crossAxisAlignment property (交叉轴对齐方式,默认都是居中?)

### CrossAxisAlignment.start
Positions children near the start of the cross axis. (Top for Row, Left for Column)

### CrossAxisAlignment.end
Positions children near the end of the cross axis. (Bottom for Row, Right for Column)

### CrossAxisAlignment.center
Positions children at the middle of the cross axis. (Middle for Row, Center for Column)

### CrossAxisAlignment.stretch
Stretches children across the cross axis. (Top-to-bottom for Row, left-to-right for Column)

### CrossAxisAlignment.baseline
Aligns children by their character baselines. (Text class only, and requires that the textBaseline property is set to TextBaseline.alphabetic. See the Text widget section for an example.)


# Flexible widget (相对,可变,窗口部件)

```dart
Flexible(
          fit: FlexFit.loose,
          flex: 1,
          child: BlueBox(),
        )

```

## flex (权值(与其他Flexible 部件相比))
Compares itself against other flex properties before determining what fraction of the total remaining space each Flexible widget receives.

remainingSpace * (flex / totalOfAllFlexValues)

## fit
Determines whether a Flexible widget fills all of its extra space.

### FlexFit.loose
The widget’s preferred size is used. (Default)

### FlexFit.tight
Forces the widget to fill all of its extra space.

# Expanded widget (强制填充满剩余空间)
```dart
 Expanded(child: BlueBox(),),
```

# SizeBox widget (改变尺寸的,或者创造定长空区域)
The SizedBox widget can be used in one of two ways when creating exact dimensions. When SizedBox wraps a widget, it resizes the widget using the height and w idth properties. When it doesn’t wrap a widget, it uses the height and width properties to create empty space.

```dart
SizedBox(
          width: 100,
          child: BlueBox(),
        ),
```

# Spacer widget (相对大小打间隔创建.或改变大小?)
Similar to SizedBox, the Spacer widget also can create space between widgets.

```dart
Spacer(flex: 1),
```
# Text widget

# Icon widget
The Icon widget displays a graphical symbol that represents an aspect of the UI. Flutter is preloaded with icon packages for Material and Cupertino applications.


# Image
Image.network
