#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri April 09 08:02:27 2021

@author: Aakash
"""

from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pusher import Pusher
import requests, json, atexit, time, plotly, plotly.graph_objs as go

    # create flask app
app = Flask(__name__)

    # configure pusher object
pusher = Pusher(
    app_id='1198323',
    key='4a2ab924c9aeb13cc8c2',
    secret='e905a1a871b086392929',
    cluster='ap2',
    ssl=True
)

    # define variables for data retrieval
times = []
currencies = ["BTC"]
prices = {"BTC": []}

@app.route("/")
def index():
    return render_template("index.html")

def retrieve_data():
        # create dictionary for saving current prices
    current_prices = {}
    for currency in currencies:
        current_prices[currency] = []
        # append new time to list of times
    times.append(time.strftime('%H:%M:%S'))

        # make request to API and get response as object
    api_url = "https://blockchain.info/ticker".format(",".join(currencies))
    response = json.loads(requests.get(api_url).content)

        # append new price to list of prices for graph
        # and set current price for bar chart
    for currency in currencies:
        price = response["USD"]["15m"]
        current_prices[currency] = price
        prices[currency].append(price)

        # create an array of traces for graph data
    graph_data = [go.Scatter(
        x=times,
        y=prices.get(currency),
        name="{} Prices".format(currency)
    ) for currency in currencies]

    data = {
        'graph': json.dumps(list(graph_data), cls=plotly.utils.PlotlyJSONEncoder)
    }

        # trigger event
    pusher.trigger("crypto", "data-updated", data)

    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=retrieve_data,
        trigger=IntervalTrigger(seconds=10),
        id='prices_retrieval_job',
        name='Retrieve prices every 10 seconds',
        replace_existing=True)
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)