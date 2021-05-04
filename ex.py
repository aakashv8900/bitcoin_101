from datetime import datetime as time
from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pusher import Pusher
import requests, json, atexit, time, plotly, plotly.graph_objs as go
times = []
currencies = ["BTC"]
prices = {"BTC": []}

def retrieve_data():
        # create dictionary for saving current prices
    current_prices = {}

        # make request to API and get response as object
    api_url = "https://blockchain.info/ticker".format(",".join(currencies))
    response = json.loads(requests.get(api_url).content)

        # append new price to list of prices for graph
        # and set current price for bar chart
    for currency in currencies:
        price = response["USD"]["15m"]
        current_prices[currency] = price
        prices[currency].append(price)


    print(prices.get(currency))

    print("------------------------------------------------------")
    print(response)

retrieve_data()