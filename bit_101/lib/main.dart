import 'dart:async';
import 'dart:ffi';
import 'package:flutter/material.dart';
import 'package:bit_101/theme/colors.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
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
            image: new AssetImage("images/backfit.jpg"),
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
                  onPressed: () {
                    Navigator.of(context).push(MaterialPageRoute(
                        builder: (BuildContext context) => MyWebView()));
                  }),
              SizedBox(
                height: 70,
              ),
              new Text(
                'Hey There! Try this app to see the real time price change of Bitcoin',
                textAlign: TextAlign.center,
                style: TextStyle(
                    color: Colors.white,
                    fontSize: 10,
                    fontWeight: FontWeight.bold),
              )
            ],
          ),
        ],
      ),
    );
  }
}

class MyWebView extends StatelessWidget {
  final Completer<WebViewController> _controller =
      Completer<WebViewController>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Live Bitcoin Price"),
        ),
        body: WebView(
          initialUrl: "https://www.digitalocean.com",
          javascriptMode: JavascriptMode.unrestricted,
          onWebViewCreated: (WebViewController webViewController) {
            _controller.complete(webViewController);
          },
        ));
  }
}
