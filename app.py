#py -m pip install dash
#py -m pip install plotly
#py -m pip install pandas

# Run `py app.py` in vscode
# visit http://127.0.0.1:8050/ in web browser

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_daq as daq
from collections import deque
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import time
import os

app = Dash(__name__)

colors = {
    'black':'#1a1a1a',
    'lightblack': '#1B1B1B',
    'red': '#da2c43',
    'mintgreen': '#98ff98',
    'green': '#007f5c',
    'yellow': '#ffef00',
    'marineblue': '#002366',
    'grey': '#808080',
    'lightgrey': '#ababab',
    'lightblue': '#58a4b0',
    'lightblue2': '#a8d0d6',
    'white': '#f1f1f1',
    'lightpurple':'#e0b0ff',
    'purple':'#873dbd',
    'orange':'#ffad01'
}

app.layout = html.Div(style={'backgroundColor': colors['black']}, children=[
    html.Div(className='block', children=[
        html.Div([
            dcc.Graph(id='live-update-graph', animate=True),
            dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0)
        ])
    ]),
    html.Div(className='block', children=[
        daq.Gauge(
            value=5,
            label='Pažnja',
            max=100,
            min=0,
        ),
        daq.Gauge(
            value=5,
            label='Meditacija',
            max=100,
            min=0,
        )
    ])
])

@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))

def get_live_updates(n):
    df = pd.read_csv('data.csv')
    mode = 'lines'
    fig = px.scatter()
    fig.add_scatter(name='Delta', y=df['delta'], mode=mode)
    fig.add_scatter(name='Theta', y=df['theta'], mode=mode)
    fig.add_scatter(name='LowAlpha', y=df['lowalpha'], mode=mode)
    fig.add_scatter(name='HighAlpha', y=df['highalpha'], mode=mode)
    fig.add_scatter(name='LowBeta', y=df['lowbeta'], mode=mode)
    fig.add_scatter(name='HighBeta', y=df['highbeta'], mode=mode)
    fig.add_scatter(name='LowGamma', y=df['lowgamma'], mode=mode)
    fig.add_scatter(name='HighGamma', y=df['highgamma'], mode=mode)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
