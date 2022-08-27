#py -m pip install dash
#py -m pip install plotly
#py -m pip install pandas

# Run `py app.py` in vscode
# visit http://127.0.0.1:8050/ in web browser

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_daq as daq
import dash_bootstrap_components as dbc
from collections import deque
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import time

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

colors = {
    'black':'#000000',
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
    'orange':'#ffad01',
    'darkgreyblue': '#232734'
}

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col(),
        dbc.Col([
            dbc.Row(dbc.Card(dbc.CardBody(dcc.Graph(id='live-update-graph', animate=True)),color=colors['lightblack'], style={'marginTop': 10, 'marginBottom': 10})),
                dbc.Row([
                    dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(id='live-update-attention', animate=True)), color=colors['lightblack'])),
                    dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(id='live-update-meditation', animate=True)),  color=colors['lightblack']))
            ])
        ])
    ]),
    dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0)
], style={'backgroundColor': colors['black'], "height":"100vh", "margin-right":0})

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
    fig1.update_xaxes(range = [0,len(df)-1])
    fig1.update_layout({"margin": {"l": 0, "r": 0, "b": 0, "t": 20}, "autosize": True}, paper_bgcolor = colors["lightblack"], plot_bgcolor=colors["lightblack"], font = {'color': colors["white"]})
    fig1.update_xaxes(showline=True, linewidth=1, linecolor=colors['darkgreyblue'], gridcolor=colors['darkgreyblue'])
    fig1.update_yaxes(showline=True, linewidth=1, linecolor=colors['darkgreyblue'], gridcolor=colors['darkgreyblue'])
    
    row = len(df)-1
    specdata1=df.iloc[row, 0]
    specdata2=df.iloc[row, 1]
  
    fig2= go.Figure(go.Indicator(
    mode = "gauge+number",
    value = specdata1,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Pažnja"},
    gauge = {'axis': {'range': [None, 100], 'tickcolor': colors['white']},
    'bar': {'color': colors["lightblue"]},
    'bgcolor': colors["lightblack"],
    'bordercolor': colors["lightblack"]
    },
    ))
    fig3 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = specdata2,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Meditacija"},
    gauge = {'axis': {'range': [None, 100], 'tickcolor': colors['white']},
    'bar': {'color': colors["lightblue"]},
    'bgcolor': colors["lightblack"],
    'bordercolor': colors["lightblack"]
    },
    ))
    fig2.update_layout({"height": 280,"autosize":False}, paper_bgcolor = colors["lightblack"], font = {'color': colors["white"]})
    fig3.update_layout({"height": 280,"autosize":False}, paper_bgcolor = colors["lightblack"], font = {'color': colors["white"]})
    return [fig1, fig2, fig3 ]


if __name__ == '__main__':
    app.run_server(debug=True)
