from dash import html, register_page, dash_table
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd  # , callback # If you need callbacks, import it here.
from dash_table import DataTable

register_page(
    __name__,
    name='Dataset',
    top_nav=True,
    path='/Dataset'
)

# Load dataset
df = pd.read_excel("New Model 3_Clusters ver 2.xlsx")


def layout():
    # Create a DataTable with pagination
    table = DataTable(
        id='table',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
        page_size=20,
        style_table={'overflowX': 'auto'},
        filter_action="native",  # Enable native filtering
        sort_action="native",  # Enable native sorting
        page_action="native",  # Enable paging
        column_selectable="single",  # Allow users to select a single column for filtering
        selected_columns=[],  # Initialize selected columns as empty
        row_selectable="multi",  # Allow multiple rows to be selected
        selected_rows=[],  # Initialize selected rows as empty
        style_data_conditional=[  # Apply some styling to the data cells
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            },
            {
                'if': {'column_editable': True},
                'backgroundColor': 'rgba(0, 116, 217, 0.3)',
                'border': '1px solid blue'
            },
            {
                'if': {'state': 'active'},
                'backgroundColor': 'rgba(0, 116, 217, 0.3)',
                'border': '1px solid blue'
            },
        ],
    )

    # Create a loading spinner while data is being loaded
    loading_spinner = dcc.Loading(
        id="loading",
        type="circle",
        children=[table],
    )

    return html.Div([html.Br(), loading_spinner])
