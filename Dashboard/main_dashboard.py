import dash
import pandas as pd
import plotly.express as px

from dash import dcc, html, Input, Output, State


investment_data_pract = {
    "Category": ["Stocks", "Alternative Investments"],
    "Value": [30000, 40000],
    "Composition": [["AAPL", "MSFT", "GOOGL"], ["Real Estate", "Lego", "Watches"]]
}


total_value = sum(investment_data_pract["Value"])
composition_pct = [value / total_value * 100 for value in investment_data_pract["Value"]]


layout = html.Div([
    html.Div([
    html.H2('Total Investment Value'),
    html.H3(f'${total_value:.2f}'),
    html.H2('Investment Composition'),
    dcc.Graph(
        id='investment-composition-graph',
        figure=px.pie(
            values=composition_pct,
            names=investment_data_pract['Category'],
            title='Investment Composition'
            )
        )
    ])
])



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

