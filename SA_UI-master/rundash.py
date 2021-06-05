import dash
import dash_core_components as dcc
import dash_html_components as html
#import Feature_files
import Classification as c
import vader as v

app = dash.Dash()
vh1= v.hotel1_average
vh2= v.hotel2_average
vh3= v.hotel3_average
vh4= v.hotel4_average

id1='2'
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Sentiment Analysis of Hotel Reviews',
                        className='nine columns offset-by-three'),
                html.Div(children='''
                    Aspect Based Analysis
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Hotel:'),
                        dcc.Checklist(
                                id = 'Cities',
                                options=[
                                    {'label': 'Hotel 1', 'value': '1'},
                                    {'label': 'Hotel 2', 'value': '2'},
                                    {'label': 'Hotel 3', 'value': '3'},
                                    {'label': 'Hotel 4', 'value': '4'}
                                ],
                                value =['1', '2', '3', '4'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph'
                )
                ], className= 'twelve columns'
                )
            ], className="row"
        ),
                        
        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Hotel:'),
                        dcc.Checklist(
                                id = 'Cities-1',
                                options=[
                                    {'label': 'Hotel 1', 'value': '1'},
                                    {'label': 'Hotel 2', 'value': '2'},
                                    {'label': 'Hotel 3', 'value': '3'},
                                    {'label': 'Hotel 4', 'value': '4'}
                                ],
                                value = ['1', '2', '3', '4'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),
        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph-1'
                )
                ], className= 'twelve columns'
                )
            ], className="row"
        ),
                        
         html.Div([
            html.Label('Please Select a Hotel from the list'),
            dcc.Dropdown(
                    id='each',
                 options=[
                     {'label': 'Hotel 1', 'value': '1'},
                     {'label': 'Hotel 2', 'value': '2'},
                     {'label': 'Hotel 3', 'value': '3'},
                     {'label': 'Hotel 4', 'value': '4'}
                 ],
                 value='1'
                 ),
        ]),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(
                            id='example-graph2',
                            figure={
                        'data': [
                            {'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel1_average, 'type': 'line', 'name': 'Hotel1'},
                            {'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel2_average, 'type': 'line', 'name': 'Hotel2'},
                            {'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel3_average, 'type': 'line', 'name': 'Hotel3'},
                            {'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel4_average, 'type': 'line', 'name': 'Hotel4'},
                        ],
                        'layout': {
                            'title': 'Graph 2'
                        }
                    }
                        ),
                    ],
                    className='thirteen columns',
                    style={'margin-top': '10'}
                ),
               
        
    ], className='ten columns offset-by-one')

])
)                    

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('Cities', 'values')])
def update_image_src(selector):
    data = []
    if '1' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel1_average, 'type': 'bar', 'name': 'Hotel1'})
    if '2' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel2_average, 'type': 'bar', 'name': 'Hotel2'})
    if '3' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel3_average, 'type': 'bar', 'name': 'Hotel3'})
    if '4' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel4_average, 'type': 'bar', 'name': 'Hotel4'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Overall Graph using Naive Bayes',
            'xaxis' : dict(
                title='Features',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Percentage',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-1', 'figure'),
    [dash.dependencies.Input('Cities-1', 'values')])
def update_image_src(selector):
    data = []
    if '1' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': vh1, 'type': 'bar', 'name': 'Hotel1'})
    if '2' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': vh2, 'type': 'bar', 'name': 'Hotel2'})
    if '3' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': vh3, 'type': 'bar', 'name': 'Hotel3'})
    if '4' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': vh4, 'type': 'bar', 'name': 'Hotel4'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Overall Graph using Vader Sentiment Analysis',
            'xaxis' : dict(
                title='Features',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Percentage',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph2', 'figure'),
    [dash.dependencies.Input('each', 'value')])
def update_image_src(selector):
    data = []
    if '1' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel1_average, 'type': 'bar', 'name': 'Hotel1'})
    elif '2' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel2_average, 'type': 'bar', 'name': 'Hotel2'})
    elif '3' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel3_average, 'type': 'bar', 'name': 'Hotel3'})
    elif '4' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel4_average, 'type': 'bar', 'name': 'Hotel4'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Individual Summary of Selected Hotel',
            'xaxis' : dict(
                title='Features',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Percentage',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure



if __name__ == '__main__':
    app.run_server(debug=True)
