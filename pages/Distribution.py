from dash import dcc, html, callback, register_page, dash_table
import pandas as pd 
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Register the page
register_page(
    __name__,
    name='Distribution',
    top_nav=True,
    path='/Distribution'
)

# Load dataset
df = pd.read_excel("New Model 6_Clusters.xlsx")
# Distribution chart function
# set average score and row id
df['Provinsi'] = df.index
avg_lt = round(df['LT (m2)'].mean(), 2)
avg_hpm = round(df['Harga Tanah (m2)'].mean(), 2)
avg_distance = round(df['distance_ke_pusatkota'].mean(), 2)
# create reusable card component
def get_card_component(title, data):
    component = dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4(title),
                            html.H4(data)
                        ]), 
                        color="dark", 
                        outline=True,
                        className = 'text-dark',
                        style={'textAlign': 'center', 'margin-bottom': '20px'}
                    ),
                )
    return component



# Dropdown widget
columns = ["Kondisi Wilayah Sekitar", "Peruntukan", "Kota/Kabupaten", "Clusters", "Hak Atas Properti"]
dd = dcc.Dropdown(id="dist_column", options=[{'label': col, 'value': col} for col in columns], value="Peruntukan", clearable=False)
# create color palette
color_discrete_sequence = ['#0a9396','#94d2bd','#e9d8a6','#ee9b00', '#ca6702', '#bb3e03', '#ae2012']
# Page layout
layout = html.Div([
    
    html.H1(children='Explore Data', style={'textAlign':'center', 'padding-bottom': '20px'}),
    dbc.Row([
        get_card_component('Total Data', '{:,}'.format(len(df.index))),
        get_card_component('Avg Luas Tanah', str(avg_lt)),
        get_card_component('Avg Harga Per Meter', str(avg_hpm)),
        get_card_component('Avg Ke Pusat Kota', str(avg_distance)),
        
    ]),
    dbc.Row(
        dbc.Col([
            html.H4("Distribusi Data Numerikal"),
            html.Div(
                dbc.RadioItems(
                    id="numerical-radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-dark",
                    labelCheckedClassName="active",
                    options=[
                        {'label': 'Luas Tanah', 'value': 'LT (m2)'},
                        {'label': 'Harga Per Meter', 'value': 'Harga Tanah (m2)'},
                        {'label': 'Jarak Pusat Kota', 'value': 'distance_ke_pusatkota'},
                        ],
                    value='LT (m2)',
                ),
                className ="radio-group",
                style = {'margin-top': '20px'}
            ),
            dcc.Graph(figure={}, id="distribution-numerical-histogram")
        ])
    ),
    dbc.Row([
        html.H4("Each Score Relationship"),
        dbc.Col(
            dcc.Graph(figure=px.scatter(df, x="LT (m2)", y="Harga Tanah (m2)", color_discrete_sequence=['#94d2bd'])),
        ),
        dbc.Col(
            dcc.Graph(figure=px.scatter(df, x="distance_ke_pusatkota", y="LT (m2)", color_discrete_sequence=['#e9d8a6'])),
        ),
        dbc.Col(
            dcc.Graph(figure=px.scatter(df, x="Harga Tanah (m2)", y="distance_ke_pusatkota", color_discrete_sequence=['#ee9b00'])),
        )
    ]),
    dbc.Row(
        dbc.Col([
            html.H4("Explore Categorical Data"),
            html.Div(
                dbc.RadioItems(
                    id="categorical-radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-dark",
                    labelCheckedClassName="active",
                    options=[
                        {'label': 'Peruntukan', 'value': 'Peruntukan'},
                        {'label': 'Kondisi Wilayah Sekitar', 'value': 'Kondisi Wilayah Sekitar'},
                        {'label': 'Kota/Kabupaten', 'value': 'Kota/Kabupaten'},
                        {'label': 'Air', 'value': 'Air_Label'},
                        {'label': 'Listrik', 'value': 'Listrik_Label'},
                    ],
                    value='Peruntukan',
                ),
                className ="radio-group",
                style = {'margin-top': '20px'}
            ),
            dcc.Graph(figure={}, id="categorical-summary"),
            dbc.Row([
                dbc.Col(dcc.Graph(figure={}, id="peruntukan-distribution")),
                dbc.Col(dcc.Graph(figure={}, id="kws-distribution")),
                dbc.Col(dcc.Graph(figure={}, id="kota-kabupaten-distribution")),
                dbc.Col(dcc.Graph(figure={}, id="air-distribution")),
                dbc.Col(dcc.Graph(figure={}, id="listrik-distribution")),
            ]),
        ])
    ),
])

# Callback to update the histogram based on selected numerical column
@callback(
    Output("distribution-numerical-histogram", "figure"),
    [Input("numerical-radios", "value")]
)
def update_histogram(selected_column):
    fig = px.histogram(df, x=selected_column, color_discrete_sequence=color_discrete_sequence)
    fig.update_layout(title=f"Distribution of {selected_column}", xaxis_title=selected_column, yaxis_title="Count")
    return fig

@callback(
    Output("categorical-summary", "figure"),
    Output("peruntukan-distribution", "figure"),
    Output("kws-distribution", "figure"),
    Output("kota-kabupaten-distribution", "figure"),
    Output("air-distribution", "figure"),
    Output("listrik-distribution", "figure"),
    [Input("categorical-radios", "value")]
)
def update_categorical_component(selected_column):
    grouped_df = pd.DataFrame({'count': df.groupby([selected_column]).size()}).reset_index()
    figure = px.bar(grouped_df, x=selected_column, y='count', color=selected_column, color_discrete_sequence=color_discrete_sequence, title='Summary')

    peruntukan_distribution = px.box(df, x=selected_column, y="Harga Tanah (m2)", color_discrete_sequence=['#0a9396'], title='Peruntukan Distribution')
    kws_distribution = px.box(df, x=selected_column, y="LT (m2)", color_discrete_sequence=['#ee9b00'], title='Kondisi Wilayah Sekitar Distribution')
    kota_kabupaten_distribution = px.box(df, x=selected_column, y="distance_ke_pusatkota", color_discrete_sequence=['#bb3e03'], title='Kota/Kabupaten Distribution')
    air_distribution = px.box(df, x=selected_column, y="Air_Label", color_discrete_sequence=['#ca6702'], title='Air Distribution')
    listrik_distribution = px.box(df, x=selected_column, y="Listrik_Label", color_discrete_sequence=['#ae2012'], title='Listrik Distribution')

    return figure, peruntukan_distribution, kws_distribution, kota_kabupaten_distribution, air_distribution, listrik_distribution
