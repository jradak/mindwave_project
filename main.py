#py pip install dash
# Run `py app.py` in vscode
# visit http://127.0.0.1:8050/ in web browser

from dash import Dash, dcc, html

app = Dash(__name__)

colors = {
    'lightblack': '#1B1B1B',
    'red': '#da2c43',
    'mintgreen': '#98ff98',
    'green': '#007f5c',
    'yellow': '#ffef00',
    'marineblue': '#002366',
    'grey': '#808080',
    'lightgrey': '#ababab',
    'lightblue': '#58a4b0',
    'white': '#f1f1f1',
    'lightpurple':'#e0b0ff',
    'purple':'#873dbd',
    'orange':'#ffad01'
}

app.layout = html.Div(style={'backgroundColor': colors['lightblack']}, children=[
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
