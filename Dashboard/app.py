"""
Main app to navigate the different tabs
"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Imports layouts for each tab
from main_dashboard import layout as main_layout
from trading import layout as trading_layout
from stocks import layout as stocks_layout
from alternative_investments import layout as alternative_layout


app = dash.Dash(__name__)

centre_style = {"text_align": "center"}

# Defined layout of dashboard
app.layout = html.Div([
    html.H1('Investment Portfolio', style={'margin': 'auto', 'text-align': 'center'}),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Overview', value='tab-1'),
        dcc.Tab(label='Trading', value='tab-2'),
        dcc.Tab(label='Stocks', value='tab-3'),
        dcc.Tab(label='Alternative Investments', value="tab-4")
    ]),
    html.Div(id='tabs-content')
])




# Callback to update tab content
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])


def update_tab_content(tab):
    if tab == 'tab-1':
        return main_layout
    elif tab == 'tab-2':
        return trading_layout
    elif tab == 'tab-3':
        return stocks_layout
    elif tab == 'tab-4':
        return alternative_layout


if __name__ == '__main__':
    app.run_server(debug=True)



