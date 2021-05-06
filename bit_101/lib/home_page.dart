import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async' show Future;
import '';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List currencies;

  @override
  void initState() {
    super.initState();
    currencies = await getCurrencies();
  }

  Future<List> getCurrencies() async {
    String cryptoUrl = "https://api.coindesk.com/v1/bpi/currentprice.json";
    http.Response response = await http.get(cryptoUrl);
    return JSON.decode(response.body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: new AppBar(
        title: new Text("Bit 101"),
      ),
      body: _cryptoWidget(),
    );
  }

  Widget _cryptoWidget() {
    return new Container(
      child: new Flexible(
        child: new ListView.builder(
          itemCount: 0,
          itemBuilder: (BuildContext context, int index) {},
        ),
      ),
    );
  }
}
