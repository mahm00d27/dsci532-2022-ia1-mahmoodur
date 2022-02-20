from dash import Dash, html, dcc, Input, Output
import altair as alt
import pandas as pd
alt.data_transformers.enable('no_max_rows')

# Read in global data
wine = pd.read_csv('data/winemag-data_first150k.csv')

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='price',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in wine.columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(wine).mark_point().encode(
        x=xcol,
        y='point',
        tooltip='price').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)

