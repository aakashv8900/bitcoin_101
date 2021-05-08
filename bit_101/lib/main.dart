import 'package:flutter/material.dart';
import 'package:bit_101/theme/colors.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primaryColor: primary,
      ),
      home: HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Bit 101"),
      ),
      body: new Stack(
        fit: StackFit.expand,
        children: <Widget>[
          new Image(
            image: new AssetImage("images/back.png"),
            fit: BoxFit.cover,
          ),
          new Column(
            children: <Widget>[
              new Image(image: new AssetImage("images/bit.png")),
              new MaterialButton(
                height: 60.0,
                minWidth: 100.0,
                color: Colors.greenAccent,
                textColor: Colors.black,
                child: new Text("Check This Out."),
                onPressed: () => {},
              ),
            ],
          ),
        ],
      ),
    );
  }
}
