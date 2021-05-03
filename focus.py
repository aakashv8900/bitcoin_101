import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

def data_importing():
    response = requests.get("https://blockchain.info/ticker")
    data = response.json()
        

    dates = []
    open_data = []

    for dataa in data:
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%d/%m/%Y, %H:%M:%S")
        dates.append(timestamp)
        dataaa = data['INR']["15m"]
        open_data.append(dataaa)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.DataFrame({
    "Time": [dates],
    "Price": [open_data]
})

fig = px.line(df, x="Time", y="Price", color="City")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)