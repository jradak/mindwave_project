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
            dcc.Graph(id='live-update-graph', animate=True)
        ])
    ]),
    html.Div(className='block', children=[
       dcc.Graph(id='live-update-attention', animate=True),
       dcc.Graph(id='live-update-meditation', animate=True)
    ]),
    dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0)
])

@app.callback([Output('live-update-graph', 'figure'), 
Output('live-update-attention', 'figure'), 
Output('live-update-meditation', 'figure')],
              Input('interval-component', 'n_intervals'))
def get_live_updates(n):
    df = pd.read_csv('data.csv')
    mode = 'lines'
    fig1 = px.scatter()
    fig1.add_scatter(name='Delta', y=df['delta'], mode=mode)
    fig1.add_scatter(name='Theta', y=df['theta'], mode=mode)
    fig1.add_scatter(name='LowAlpha', y=df['lowalpha'], mode=mode)
    fig1.add_scatter(name='HighAlpha', y=df['highalpha'], mode=mode)
    fig1.add_scatter(name='LowBeta', y=df['lowbeta'], mode=mode)
    fig1.add_scatter(name='HighBeta', y=df['highbeta'], mode=mode)
    fig1.add_scatter(name='LowGamma', y=df['lowgamma'], mode=mode)
    fig1.add_scatter(name='HighGamma', y=df['highgamma'], mode=mode)

    row = len(df)-1
    specdata1=df.iloc[row, 0]
    specdata2=df.iloc[row, 1]
    # fig2= px.scatter()
    # fig2.add_scatter(name='Attention', y=df['attention'], mode=mode)
    # fig3= px.scatter()
    # fig3.add_scatter(name='Meditation', y=df['meditation'], mode=mode)
    # fig2= px.pie(values=[specdata1, 100-specdata1], hole=.3, title='Pažnja')
    # fig3= px.pie(values=[specdata2, 100-specdata2], hole=.3, title='Meditacija')
    fig2= go.Figure(go.Indicator(
    mode = "gauge+number",
    value = specdata1,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Pažnja"},
    gauge = {'axis': {'range': [None, 100]}},
    ))
    fig3 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = specdata2,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Meditacija"},
    gauge = {'axis': {'range': [None, 100]}},
    ))
    return [fig1, fig2, fig3 ]


if __name__ == '__main__':
    app.run_server(debug=True)
