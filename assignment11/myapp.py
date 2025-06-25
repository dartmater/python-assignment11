from dash import Dash, dcc, html, Input, Output
import plotly.express as px


app = Dash(__name__)
server = app.server  # Required for Render


df = px.data.gapminder()


app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in df['country'].unique()],
        value='Canada'
    ),
    dcc.Graph(id='gdp-growth')
])


@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(country):
    filtered_df = df[df['country'] == country]
    return px.line(filtered_df, x='year', y='gdpPercap', 
                 title=f'GDP per Capita: {country}')

if __name__ == '__main__':
    app.run(debug=True)