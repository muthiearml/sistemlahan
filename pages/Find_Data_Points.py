# -*- coding: utf-8 -*-
"""
Created on Fri May 31 23:51:15 2024

@author: daffa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:20:03 2024

@author: daffa
"""
from dash import html, register_page, dcc, callback
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash
from dash import dcc, html, Input, Output, State
from geopy.distance import geodesic
register_page(
    __name__,
    name='Finding Data Points',
    top_nav=True,
    path='/Find_Data_Points'
)

# DATASET
try:
    df = pd.read_excel("New Model 6_Clusters.xlsx")
except Exception as e:
    df = pd.DataFrame()  # Fallback to an empty dataframe if loading fails
    print(f"Error loading dataset: {e}")

# Create a single 'Clusters' column if not exists
if 'Clusters' not in df.columns:
    # Assuming Clusters_0, Clusters_1, and Clusters_2 are mutually exclusive, create 'Clusters' column
    df['Clusters'] = df[['Clusters_0', 'Clusters_1', 'Clusters_2']].idxmax(axis=1)

# Category mapping of cities to coordinates
category_mapping = {
    'Kabupaten Bekasi': '-6.364468, 107.172577', 'Kabupaten Bogor': '-6.480315, 106.862518', 
    'Kabupaten Bandung': '-7.027290, 107.519093','Kota Depok':'-6.373080, 106.834747','Kota Bekasi':'-6.226096, 107.000923',
    'Kota Bandung':'-6.920828338899329, 107.60706229925285','Kota Bogor':'-6.597122, 106.795200','Kabupaten Karawang':'-6.309075, 107.307121',
    'Kabupaten Subang':'-6.571596, 107.762138','Kabupaten Kuningan':'-6.977390, 108.476444','Kabupaten Bandung Barat':'-6.817989, 107.618828',
    'Kabupaten Cianjur':'-6.820688, 107.137733','Kabupaten Sukabumi':'-6.988767, 106.551907','Kabupaten Majalengka':'-6.833771, 108.233477',
    'Kota Banjar':'-7.369006, 108.543286','Kabupaten Ciamis':'-7.376872, 108.541109','Kabupaten Indramayu':'-6.393929, 108.154870',
    'Kota Cirebon':'-6.724067, 108.573402','Kabupaten Cirebon':'-6.757771, 108.480034','Kota Tasikmalaya':'-7.327277, 108.220267',
    'Kabupaten Purwakarta':'-6.556692, 107.441391','Kabupaten Tasikmalaya':'-7.3672746043290624, 108.08501947317386','Kabupaten Garut':'-7.354457602865938, 107.80601286466963',
    'Kota Sukabumi':'-6.921897, 106.923918','Kota Cimahi':'-6.872557, 107.543060','Kabupaten Pangandaran':'-7.702401, 108.496690',
    'Kabupaten Sumedang':'-6.895941, 107.809429'
}

# Function to calculate the geodesic distance using geopy
def calculate_distance(row, new_house):
    point = (row['latitude'], row['longitude'])
    return geodesic(new_house, point).kilometers

# Function to find the city based on the closest center from category_mapping
def find_city_and_distance(new_house):
    min_distance = float('inf')
    closest_city = None
    for city, coord in category_mapping.items():
        city_coord = tuple(map(float, coord.split(', ')))
        distance = geodesic(new_house, city_coord).kilometers
        if distance < min_distance:
            min_distance = distance
            closest_city = city
    return closest_city, min_distance


layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Find Closest Data Points"),
            dbc.Form([
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Latitude:"),
                        dbc.Input(id="input-latitude", type="number", value=34.0522, step=0.0001)
                    ])
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Longitude:"),
                        dbc.Input(id="input-longitude", type="number", value=-118.2437, step=0.0001)
                    ])
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col([
                        dbc.Button("Find Closest Points", id="submit-button", color="primary", className="mr-2")
                    ])
                ])
            ]),
            html.Hr(),
            html.Div(id="output-table"),
            dcc.Graph(id="map-container"),
            html.Div(id="distance-info")
        ])
    ])
])

@callback(
    [Output("output-table", "children"),
     Output("map-container", "figure"),
     Output("distance-info", "children")],
    [Input("submit-button", "n_clicks")],
    [State("input-latitude", "value"),
     State("input-longitude", "value")]
)
def update_output(n_clicks, latitude, longitude):
    if n_clicks is None:
        return "", {}, ""
    
    new_house = (latitude, longitude)
    df['distance'] = df.apply(calculate_distance, axis=1, args=(new_house,))
    df_sorted = df.sort_values('distance').reset_index(drop=True)
    num_closest = 4
    closest_data_points = df_sorted.head(num_closest)
    
    # Find the closest city and distance to it
    closest_city, city_distance = find_city_and_distance(new_house)
    
    table_header = [html.Thead(html.Tr([
        html.Th("Latitude"), 
        html.Th("Longitude"), 
        html.Th("Distance to Point (km)"), 
        html.Th("LT (m2)"), 
        html.Th("Harga Tanah (m2)"),
        html.Th("Clusters"),
        html.Th("Hak Atas Properti"),
        html.Th("Kondisi Tapak"),
        html.Th("Lebar Jalan Depan (m)"),
        html.Th("Kondisi Wilayah Sekitar"),
        html.Th("Peruntukan")
    ]))]
    
    table_body = [html.Tbody([
        html.Tr([
            html.Td(closest_data_points.iloc[i]['latitude']),
            html.Td(closest_data_points.iloc[i]['longitude']),
            html.Td(round(closest_data_points.iloc[i]['distance'], 2)),
            html.Td(closest_data_points.iloc[i]['LT (m2)']),
            html.Td(closest_data_points.iloc[i]['Harga Tanah (m2)']),
            html.Td(closest_data_points.iloc[i]['Clusters']),
            html.Td(closest_data_points.iloc[i]['Hak Atas Properti']),
            html.Td(closest_data_points.iloc[i]['Kondisi Tapak']),
            html.Td(closest_data_points.iloc[i]['Lebar Jalan Depan (m)']),
            html.Td(closest_data_points.iloc[i]['Kondisi Wilayah Sekitar']),
            html.Td(closest_data_points.iloc[i]['Peruntukan'])
        ]) for i in range(num_closest)
    ])]
    
    fig = px.scatter_mapbox(df_sorted.head(4), 
                             lat="latitude", lon="longitude", 
                             hover_name="Hak Atas Properti",
                             hover_data=["Harga Tanah (m2)", "Clusters", "Kondisi Tapak", "Lebar Jalan Depan (m)", "Kondisi Wilayah Sekitar", "Peruntukan"],
                             zoom=10, center={"lat": latitude, "lon": longitude})
    fig.update_layout(mapbox_style="carto-positron")
    
    # Add trace for inputted data point
    fig.add_trace(px.scatter_mapbox(pd.DataFrame({'latitude': [latitude], 'longitude': [longitude]}),
                                    lat="latitude", lon="longitude",
                                    text=["Inputted Data Point"]).data[0])
    
    distance_info = f"Input Coordinates: (Latitude: {latitude}, Longitude: {longitude}), Closest City: {closest_city}, Distance to City Center: {round(city_distance, 2)} km"
    
    return dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True), fig, distance_info
