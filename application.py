import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import yfinance as yf

def get_stock(stock_name):
    """
    Gets stock dataframe

    Args:
        stock_name str: Name of the stock per their NYE abbriviation

    Returns:
        dataframe
    """

    df_stock = yf.Ticker(stock_name).history(period="max")
    return df_stock

df = get_stock('MSFT').reset_index()

line_graph = px.line(data_frame=df, x=df['Date'], y=df['Close'], title='MSFT Price')

app = dash.Dash(__name__)

application = app.server

app.layout = html.Div([
    dcc.Graph(id="line-chart", figure=line_graph),
])


if __name__ == '__main__':
    # Beanstalk expects it to be running on 8080.
    application.run(debug=True, port=8080)