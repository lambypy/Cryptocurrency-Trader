import dash
from dash import dcc, html, Input, Output, State
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Investment Portfolio Dashboard"),
    html.Div([
        html.Label("Stock Symbol"),
        dcc.Input(id='stock-symbol', type='text', value='AAPL'),
        html.Label("Purchase Price"),
        dcc.Input(id='purchase-price', type='number', value=0),
        html.Label("Quantity"),
        dcc.Input(id='quantity', type='number', value=0),
        html.Button('Add to Portfolio', id='add-button', n_clicks=0),
    ]),
    html.Div(id='portfolio-table')
])

@app.callback(
    Output('portfolio-table', 'children'),
    [Input('add-button', 'n_clicks')],
    [State('stock-symbol', 'value'),
     State('purchase-price', 'value'),
     State('quantity', 'value')]
)
def update_portfolio_table(n_clicks, stock_symbol, purchase_price, quantity):
    if n_clicks > 0:
        new_entry = {'Symbol': stock_symbol, 'Purchase Price': purchase_price, 'Quantity': quantity}
        portfolio_df = pd.DataFrame([new_entry])
        return html.Table([
            html.Thead(html.Tr([html.Th(col) for col in portfolio_df.columns])),
            html.Tbody([
                html.Tr([
                    html.Td(portfolio_df.iloc[i][col]) for col in portfolio_df.columns
                ]) for i in range(len(portfolio_df))
            ])
        ])
    else:
        return html.Table()

if __name__ == '__main__':
    app.run_server(debug=True)