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
        primaryColor: Colors.black,
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
        title: Text("Bitcoin 101"),
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
              new Text(
                'Bitcoin 101',
                textAlign: TextAlign.center,
                style: TextStyle(
                    color: Colors.white,
                    fontSize: 40,
                    fontWeight: FontWeight.bold),
              ),
              SizedBox(
                height: 30,
              ),
              new Text(
                'Real Time Bitcoin Price in 1 minute',
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 20,
                  fontWeight: FontWeight.w100,
                ),
              ),
              new Text(
                'interval for the last 24 hours.',
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 20,
                  fontWeight: FontWeight.w100,
                ),
              ),
              SizedBox(
                height: 30,
              ),
              new MaterialButton(
                  height: 60.0,
                  minWidth: 100.0,
                  color: primary,
                  textColor: Colors.black,
                  child: new Text("Check It Out."),
                  onPressed: () {
                    Navigator.of(context).push(MaterialPageRoute(
                        builder: (BuildContext context) => MyWebView()));
                  }),
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
          initialUrl: "https://bitcoinpricelivechart.azurewebsites.net/",
          javascriptMode: JavascriptMode.unrestricted,
          onWebViewCreated: (WebViewController webViewController) {
            _controller.complete(webViewController);
          },
        ));
  }
}
