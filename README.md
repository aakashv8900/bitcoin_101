<p align = "center">
<h1 align="center">Bitcoin 101</h1>
</p>
<img src="read.gif">

# Details

<h3 align="center">Basically this project is divided into two parts.</h3>

•	Bitcoin Price Live Chart – In this portion of this project I connected the Binance Crypto API which is a streaming data API, to a javascript websocket and then gave that data to Light Weighted Trading View Candlestick Chart. When this whole process completed, I implemented that live chart to a Flask framework and then containerized the whole framework with chart by Docker and deployed to Azure. 

Link of deployment - https://bitcoinpricelivechart.azurewebsites.net/ 

•	Flutter App – In this portion of this project I created a basic Flutter app in which the user gets an interactive front page with a button on that page. When the user clicked that button, the Bitcoin Price Live Chart which is deployed on Azure renders in a webview page of this flutter app. 

By this the user gets the live price change of Bitcoin Crypto Currency on their cell phone by just clicking a single button.
