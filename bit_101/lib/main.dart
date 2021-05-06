import 'package:bit_101/home_page.dart';
import 'package:flutter/material.dart';

void main() => runApp(new Myapp());

class Myapp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: new ThemeData(primarySwatch: Colors.blueGrey),
      home: new HomePage(),
    );
  }
}
