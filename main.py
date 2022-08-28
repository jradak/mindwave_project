#py -m pip install dash
#py -m pip install plotly
#py -m pip install pandas

# Run `py app.py` in vscode
# visit http://127.0.0.1:8050/ in web browser

from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import csv
import reader
import sys
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

colors = {
    'black':'#000000',
    'lightblack': '#1B1B1B',
    'shadow':'#333333',
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
        dbc.Col([
            dbc.Card(dbc.CardBody(dcc.Upload(
                id='upload-image',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px',
                    'color': colors['white']
                },
                multiple=True
                )), color=colors['lightblack'], style={'marginTop': 10, 'marginBottom': 10}),
                html.Div(id='output-image-upload', style={"textAlign":'center'}),
        ]),
        dbc.Col(
            dbc.Card(dbc.CardBody(dcc.Graph(id='live-update-graph', animate=True)),color=colors['lightblack'], style={'marginTop': 10, 'marginBottom': 10})
        ),
        dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0)
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.Div(
                    html.I(className="bi bi-emoji-laughing-fill"),
                    style={"color": colors["shadow"], "fontSize": 62,},
                    id='happy'
                ),
                html.Div(
                    html.I(className="bi bi-emoji-neutral-fill"),
                    style={"color": colors["lightblue"], "fontSize": 62},
                    id='neutral'
                ),
                html.Div(
                    html.I(className="bi bi-emoji-frown-fill"),
                    style={"color": colors["shadow"], "fontSize": 62,},
                    id='sad'
                )
        ],), color=colors['lightblack'], style={"textAlign": "center"})
        ),
        dbc.Col([
            dbc.Card(dbc.CardBody([
                dbc.RadioItems(
                    options=[
                        {"label": "Pozitivno", "value": 'pozitivno'},
                        {"label": "Neutralno", "value": 'neutralno'},
                        {"label": "Negativno", "value": 'negativno'},
                    ],
                    value='neutralno',
                    label_style={"color": colors['white'], 'fontSize': 20},
                    input_style={
                        "backgroundColor": colors['black'],
                        "borderColor": colors['black'],
                    },
                    label_checked_style={"color": colors['lightblue']},
                    input_checked_style={
                        "backgroundColor": colors['lightblue'],
                        "borderColor": colors['lightblack'],
                    },
                    style={"marginTop": 40, "marginBottom": 40},
                    id="radioitems-input"
                ),
                dcc.Interval(id='interval-component2', interval=1*1000, n_intervals=0, disabled=True, max_intervals=15),
                dbc.ButtonGroup([
                    dbc.Button(html.I(className="bi bi-play"), id="btn-play", n_clicks=0, color="light",style={"backgroundColor": colors["lightblue"], "color": colors["lightblack"], "border":"none"}), 
                    dbc.Button(html.I(className="bi bi-download"), id="btn-download", n_clicks=0, color="light", style={"backgroundColor": colors["lightblue"], "color": colors["lightblack"], "border":"none"}), 
                    dbc.Button(html.I(className="bi bi-arrow-right"), id="btn-forward", n_clicks=0, color="light", style={"backgroundColor": colors["lightblue"], "color": colors["lightblack"], "border":"none"})
                ], size="lg",style={"marginTop": 10, "marginBottom": 10}),
                html.Div(id='output-csv'),
                html.Div(id='download-csv', style={"marginTop": 10, "marginBottom": 10}),
            ]),
            color=colors['lightblack'], style={"textAlign":"center"})
        ]),
        dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(id='live-update-attention', animate=True)), color=colors['lightblack'])),
        dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(id='live-update-meditation', animate=True)), color=colors['lightblack']))
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Button(html.I(className='bi bi-eye'),id="btn-model", n_clicks=0,color="dark",style={"backgroundColor": colors["lightblack"], "color": colors["lightblue"], "border":"none", 'fontSize':20}),
            dbc.Button(html.I(className='bi bi-headset'),id="btn-connect", n_clicks=0,color="dark",style={"backgroundColor": colors["lightblack"], "color": colors["lightblue"], "border":"none", 'fontSize':20}),
            html.A(dbc.Button(html.I(className='bi bi-arrow-clockwise'),id="btn-refresh-page", n_clicks=0,color="dark",style={"backgroundColor": colors["lightblack"], "color": colors["lightblue"], "border":"none", 'fontSize':20}), href='/' ),
            dbc.Modal(
                [
                    dbc.ModalBody(dcc.Graph(id="knn-graph"), style={"backgroundColor": colors["lightblack"], "color":colors["white"],"border":'none'}),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Zatvori", id="close", className="ms-auto", n_clicks=0, color="dark",style={"backgroundColor": colors["lightblack"], "color": colors["lightblue"], "border":"none", 'fontSize':20}
                        ), style={"backgroundColor": colors["lightblack"], "color":colors["white"],"border":'none'}
                    ),
                ],id="modal",is_open=False
            ),
            html.Div(id="connect-output")
        ], style={"textAlign":"right"})
    ], style={'marginTop':10} )
], style={'backgroundColor': colors['black']})

def parse_contents(contents, filename, date):
    return html.Div([
        html.Img(src=contents, style={'height':'60%', 'width':'60%'}),
    ])

def write_csv(name):
    fieldnames = ["attention", "meditation", "delta", "theta", "lowalpha", "highalpha", "lowbeta", "highbeta", "lowgamma", "highgamma" ]
    with open(name, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

write_csv('pozitivno.csv')
write_csv('neutralno.csv')
write_csv('negativno.csv')

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

@app.callback(Output('output-image-upload', 'children'),
              Input("btn-forward", "n_clicks"),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(n, list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        if n is None:
            return children[0]
        else:
            if len(list_of_contents)-1 < n:
                n=0
            return children[n]

new_data=[]
@app.callback([Output('interval-component2', 'n_intervals'), Output('interval-component2', 'disabled')],
                Input('btn-play','n_clicks'))
def start_count(n_play):
    if n_play is None:
        return
    elif n_play!=0 and n_play!=None and n_play%2!=0:
        return 0, False
    else:
        new_data.clear()
        return 0, True
    
@app.callback(Output('output-csv','children'), Input('interval-component2', 'n_intervals'))
def updateCsv(n_intervals):
        input_csv=pd.read_csv('data.csv')
        sub_array=[]
        row = len(input_csv)-1
        spec_dat=input_csv.iloc[row]
        sub_array.append(spec_dat["attention"])
        sub_array.append(spec_dat["meditation"])
        sub_array.append(spec_dat["delta"])
        sub_array.append(spec_dat["theta"])
        sub_array.append(spec_dat["lowalpha"])
        sub_array.append(spec_dat["highalpha"])
        sub_array.append(spec_dat["lowbeta"])
        sub_array.append(spec_dat["highbeta"])
        sub_array.append(spec_dat["lowgamma"])
        sub_array.append(spec_dat["highgamma"])
        new_data.append(sub_array)
        return  html.Div("Broj zapisa: {}".format(n_intervals), style={'color': colors['white'], 'fontSize':20})

@app.callback(Output('download-csv', 'children'),
            [Input('btn-download','n_clicks'), Input('radioitems-input', 'value')])
def save_csv(n_download, value):
    if n_download is None:
        return
    if n_download>0 and n_download is not None:
        fieldnames = ["attention", "meditation", "delta", "theta", "lowalpha", "highalpha", "lowbeta", "highbeta", "lowgamma", "highgamma" ]
        with open('{}.csv'.format(value), 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            for row in range(len(new_data)):
                info={
                    "attention": new_data[row][0],
                    "meditation": new_data[row][1],
                    "delta": new_data[row][2], 
                    "theta": new_data[row][3], 
                    "lowalpha": new_data[row][4], 
                    "highalpha": new_data[row][5], 
                    "lowbeta": new_data[row][6], 
                    "highbeta": new_data[row][7], 
                    "lowgamma": new_data[row][8], 
                    "highgamma": new_data[row][9]
                }
                csv_writer.writerow(info)
            new_data.clear()            

@app.callback(
    Output("modal", "is_open"),
    [Input("btn-model", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(Output("connect-output", "children"), Input("btn-connect", "n_clicks"))
def connect(n):
    if n is None or n == 0:
        return
    elif n!=0 and n is not None:
        if n%2!=0:
            reader.start()
        if n%2!=1:
            sys.exit()
    else:
        return

if __name__ == '__main__':
    app.run_server(debug=True)
