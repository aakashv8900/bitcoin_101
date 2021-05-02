import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import requests
import plotly
import random
import plotly.express as px
import plotly.graph_objs as go
from collections import deque

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/INR.json")
data = response.json()
price = data['bpi']['INR']['rate_float']
time = data['time']['updated']

app = dash.Dash(__name__, data=data, price=price, time=time)
app.layout = html.Div(
    [
        html.Div([
            dcc.Input(
                id='xaxis-column',
                value='Time'
            ),
            dcc.Input(
                id='yaxis-column',
                value='Price',
            )
        ]),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*100
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
                Input('xaxis-column', 'value'),
                Input('yaxis-column', 'value'),
              events=('graph-update', 'interval'))
def update_graph_scatter(xaxis_column, yaxis_column):


    data = plotly.graph_objs.Scatter(
            x=xaxis-column,
            y=yaxis-column,
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}



if __name__ == '__main__':
    app.run_server(debug=True)