from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

app = Dash(__name__,external_stylesheets=['styles.css'])

# line_fig = px.line(happiness[happiness['country']=='India'], x='year',
#                              y='happiness_score',title='Happiness Score in India')
app.layout = html.Div([

    html.Div([
        html.H1("World Happiness Index Dashboard"),
        # html.Img(src="/assets/happiness.png")
        ]),




    html.H4(["This Dashboard shows the Happiness Index of countries the listed below:",
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href = 'https://worldhappiness.report',
                   target='_blank')]),
    # dcc.RadioItems(options= happiness['region'].unique(), value='India'),
    # dcc.Checklist(options=happiness['region'].unique(), value=['India']),
    dcc.Dropdown(id='country-dropdown', options=  happiness['country'].unique(),
                 value='India',className='my-dropdown'),
    dcc.Graph(id='happiness-graph', figure={})

])



@app.callback(
    Output(component_id = 'happiness-graph', component_property= 'figure'),
    Input(component_id = 'country-dropdown', component_property= 'value'))


def update_graph(select_country):
    filtered_happiness = happiness[happiness['country'] == select_country]
    line_fig = px.line(filtered_happiness, x='year',y= 'happiness_score',
                       title=f'Happiness Score in {select_country}')
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)
