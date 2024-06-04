# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:22:36 2024

@author: daffa
"""
from dash import html, register_page, dcc, callback
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

register_page(
    __name__,
    name='Relationship',
    top_nav=True,
    path='/Relationship'
)

####################### DATASET #############################
df = pd.read_excel("New Model 3_Clusters.xlsx")

####################### SCATTER CHART #############################
def create_scatter_chart(x_axis="Peruntukan", y_axis="LT (m2)", color_axis="Clusters"):
    return px.scatter(data_frame=df, x=x_axis, y=y_axis, color=color_axis, height=600)

####################### WIDGETS #############################
columns = ["LT (m2)", "Kondisi Wilayah Sekitar", "Harga Tanah (m2)", "distance_ke_pusatkota", "Air", "Listrik", "Peruntukan", "Kota/Kabupaten", "Clusters", "Hak Atas Properti"]

x_axis = dcc.Dropdown(id="x_axis", options=[{'label': col, 'value': col} for col in columns], value="Harga Tanah (m2)", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=[{'label': col, 'value': col} for col in columns], value="distance_ke_pusatkota", clearable=False)
color_dropdown = dcc.Dropdown(id="color_dropdown", options=[{'label': col, 'value': col} for col in columns], value="Peruntukan", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    "X-Axis", x_axis,
    "Y-Axis", y_axis,
    "Color By", color_dropdown,
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@callback(
    Output("scatter", "figure"),
    [Input("x_axis", "value"), Input("y_axis", "value"), Input("color_dropdown", "value")]
)
def update_scatter_chart(x_axis, y_axis, color_by):
    print("X-Axis:", x_axis)
    print("Y-Axis:", y_axis)
    print("Color By:", color_by)
    try:
        return create_scatter_chart(x_axis, y_axis, color_by)
    except Exception as e:
        print("Error:", e)
        return {}
