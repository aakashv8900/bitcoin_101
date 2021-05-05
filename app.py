#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri April 09 08:02:27 2021

@author: Aakash
"""

import flask
from flask import Flask, url_for, request, render_template, jsonify
import os
from flask import Flask
from binance.client import Client
client = Client('sgoLhBuGcqkgY7TNFaRVoL0xrW9lfx0WCARDd0QzCdEAOC1PMUt00WzmZu8dbQo9', 'SqRrVJrfr2e7gHCsS1WjgBzxTXA4duZdFMaLOADCunVFbNkOfzlQFs8g9OWPFBHm')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/history")
def history():
    candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "3 Jan, 2009", "1 day ago UTC")
    processed = []
    for data in candles:
        candle = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4]
        }

        processed.append(candle)
    return jsonify(processed)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)