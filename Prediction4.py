# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:30:51 2024

@author: daffa
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:51:36 2024

@author: daffa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:27:42 2024

@author: daffa
"""
from dash import register_page,dash_table,dcc, html, callback
import pandas as pd 
import plotly.express as px
from dash.dependencies import Input, Output, State #, callback # If you need callbacks, import it here.
import joblib
import numpy as np

register_page(
    __name__,
    name='Prediction 4 Clusters',
    top_nav=True,
    path='/Prediction4'
)
####################### DATASET #############################
# Load the model from the file
loaded_model = joblib.load("New Model 4 Clusters.joblib")
loaded_scaler = joblib.load('New Model 4 Clusters Scaler.joblib')

####################### PAGE LAYOUT #############################
####################### PAGE LAYOUT #############################
# Updated layout with dropdown options based on one-hot encoding
layout = html.Div([
    html.H1("Random Forest Regressor Prediction App"),
    dcc.Input(id='lt-input', type='number', placeholder='Enter LT (m2)'),
    dcc.Dropdown(id='air-label-dropdown',
                options=[
                    {'label': 'Tidak Ada', 'value': 0},
                    {'label': 'Ada', 'value': 1},
                ],
                placeholder='Select Ketersediaan Air'
                ),
    dcc.Dropdown(id='listrik-label-dropdown',
                options=[
                    {'label': 'Tidak Ada', 'value': 0},
                    {'label': 'Ada', 'value': 1},
                ],
                placeholder='Select Ketersediaan Listrik'
                ),
    dcc.Input(id='distance-input', type='number', placeholder='Enter distance_ke_pusatkota'),
    #dcc.Dropdown(id='Distance-Category-Label-dropdown',
     #           options=[
      #              {'label': 'Dekat', 'value': 3},
       #             {'label': 'Sedang', 'value': 2},
        #            {'label': 'Jauh', 'value': 1},
         #           {'label': 'Sangat Jauh', 'value': 0},
          #      ],   
           #     placeholder='Select Kategori Jarak Pusat Kota'
            #    ),
  #  
   dcc.Input(id='lebar-jalan-input', type='number', placeholder='Enter Lebar Jalan Depan (m)'),
   dcc.Dropdown(
       id='clusters-dropdown',
       options=[
           {'label': f'Cluster_{i}', 'value': i} for i in range(4)
       ],
       placeholder='Select Clusters'
   ),
   dcc.Dropdown(
       id='peruntukan-dropdown',
       options=[
           {'label': 'Fasilitas Umum', 'value': 'Peruntukan_Fasilitas Umum'},
           {'label': 'Kawasan Industri', 'value': 'Peruntukan_Kawasan Industri'},
           {'label': 'Kawasan Perdagangan dan Jasa', 'value': 'Peruntukan_Kawasan Perdagangan dan Jasa'},
           {'label': 'Kawasan Peruntukan Perkebunan', 'value': 'Peruntukan_Kawasan Peruntukan Perkebunan'},
           {'label': 'Pemukiman Perkotaan', 'value': 'Peruntukan_Pemukiman Perkotaan'},
       
       ],
       placeholder='Select Peruntukan'
   ),
   dcc.Dropdown(
       id='hap-dropdown',
       options=[
           {'label': 'Hak Atas Properti_AJB', 'value': 'Hak Atas Properti_AJB'},
           {'label': 'Hak Atas Properti_Girik', 'value': 'Hak Atas Properti_Girik'},
         #  {'label': 'Hak Atas Properti_Gross Akte', 'value': 'Hak Atas Properti_Gross Akte'},
           {'label': 'Hak Atas Properti_HGB diatas HPL', 'value': 'Hak Atas Properti_HGB diatas HPL'},
           {'label': 'Hak Atas Properti_HP', 'value': 'Hak Atas Properti_HP'},
           {'label': 'Hak Atas Properti_PPJB', 'value': 'Hak Atas Properti_PPJB'},
           
           {'label': 'Hak Atas Properti_SHGB', 'value': 'Hak Atas Properti_SHGB'},
         #  {'label': 'Hak Atas Properti_SHGU', 'value': 'Hak Atas Properti_SHGU'},
           {'label': 'Hak Atas Properti_SHM', 'value': 'Hak Atas Properti_SHM'},
           
           {'label': 'Hak Atas Properti_SHMSRS ', 'value': 'Hak Atas Properti_SHMSRS '},
           {'label': 'Hak Atas Properti_SIPPT', 'value': 'Hak Atas Properti_SIPPT'},
        #   {'label': 'Hak Atas Properti_SPH', 'value': 'Hak Atas Properti_SPH'},
       ],
       placeholder='Select Hak Atas Properti'
   ),
    dcc.Dropdown(
    id='kota-kabupaten-dropdown',
    options=[
        {'label': 'Kabupaten Bandung', 'value': 'Kota/Kabupaten_Kabupaten Bandung'},
        {'label': 'Kabupaten Bandung Barat', 'value': 'Kota/Kabupaten_Kabupaten Bandung Barat'},
        {'label': 'Kabupaten Bekasi', 'value': 'Kota/Kabupaten_Kabupaten Bekasi'},
        {'label': 'Kabupaten Bogor', 'value': 'Kota/Kabupaten_Kabupaten Bogor'},
        {'label': 'Kabupaten Ciamis', 'value': 'Kota/Kabupaten_Kabupaten Ciamis'},
        {'label': 'Kabupaten Cianjur', 'value': 'Kota/Kabupaten_Kabupaten Cianjur'},
        {'label': 'Kabupaten Cirebon', 'value': 'Kota/Kabupaten_Kabupaten Cirebon'},
        {'label': 'Kabupaten Garut', 'value': 'Kota/Kabupaten_Kabupaten Garut'},
        {'label': 'Kabupaten Indramayu', 'value': 'Kota/Kabupaten_Kabupaten Indramayu'},
        {'label': 'Kabupaten Karawang', 'value': 'Kota/Kabupaten_Kabupaten Karawang'},
        {'label': 'Kabupaten Kuningan', 'value': 'Kota/Kabupaten_Kabupaten Kuningan'},
        {'label': 'Kabupaten Majalengka', 'value': 'Kota/Kabupaten_Kabupaten Majalengka'},
        {'label': 'Kabupaten Pangandaran', 'value': 'Kota/Kabupaten_Kabupaten Pangandaran'},
        {'label': 'Kabupaten Purwakarta', 'value': 'Kota/Kabupaten_Kabupaten Purwakarta'},
        {'label': 'Kabupaten Subang', 'value': 'Kota/Kabupaten_Kabupaten Subang'},
        {'label': 'Kabupaten Sukabumi', 'value': 'Kota/Kabupaten_Kabupaten Sukabumi'},
        {'label': 'Kabupaten Sumedang', 'value': 'Kota/Kabupaten_Kabupaten Sumedang'},
        {'label': 'Kabupaten Tasikmalaya', 'value': 'Kota/Kabupaten_Kabupaten Tasikmalaya'},
        {'label': 'Kota Bandung', 'value': 'Kota/Kabupaten_Kota Bandung'},
        {'label': 'Kota Banjar', 'value': 'Kota/Kabupaten_Kota Banjar'},
        {'label': 'Kota Bekasi', 'value': 'Kota/Kabupaten_Kota Bekasi'},
        {'label': 'Kota Bogor', 'value': 'Kota/Kabupaten_Kota Bogor'},
        {'label': 'Kota Cimahi', 'value': 'Kota/Kabupaten_Kota Cimahi'},
        {'label': 'Kota Cirebon', 'value': 'Kota/Kabupaten_Kota Cirebon'},
        {'label': 'Kota Depok', 'value': 'Kota/Kabupaten_Kota Depok'},
        {'label': 'Kota Sukabumi', 'value': 'Kota/Kabupaten_Kota Sukabumi'},
        {'label': 'Kota Tasikmalaya', 'value': 'Kota/Kabupaten_Kota Tasikmalaya'},
    ],
    placeholder='Select Kota/Kabupaten'
),

    
    
    dcc.Dropdown(
        id='bentuk-tapak-dropdown',
        options=[
            {'label': 'Kipas', 'value': 'Bentuk Tapak_Kipas'},
            {'label': 'Letter L', 'value': 'Bentuk Tapak_Letter L'},
            {'label': 'Ngantong', 'value': 'Bentuk Tapak_Ngantong'},
            {'label': 'Persegi', 'value': 'Bentuk Tapak_Persegi'},
            {'label': 'Persegi Panjang', 'value': 'Bentuk Tapak_Persegi Panjang'},
            {'label': 'Tidak Beraturan', 'value': 'Bentuk Tapak_Tidak Beraturan'},
            {'label': 'Trapesium', 'value': 'Bentuk Tapak_Trapesium'},
        ],
        placeholder='Select Bentuk Tapak'
    ),
   # dcc.Dropdown(
    #    id='kualitas-wilayah-dropdown',
     #   options=[
      #      {'label': 'Bawah', 'value': 'Kualitas Wilayah Sekitar_Bawah'},
       #     {'label': 'Kumuh', 'value': 'Kualitas Wilayah Sekitar_Kumuh'},
        #    {'label': 'Menengah', 'value': 'Kualitas Wilayah Sekitar_Menengah'},
         #   {'label': 'Mewah', 'value': 'Kualitas Wilayah Sekitar_Mewah'},
        #],
        #placeholder='Select Kualitas Wilayah Sekitar'
    #),
    dcc.Dropdown(
        id='kondisi-wilayah-dropdown',
        options=[
            {'label': 'Campuran', 'value': 'Kondisi Wilayah Sekitar_Campuran'},
            {'label': 'Hijau', 'value': 'Kondisi Wilayah Sekitar_Hijau'},
            {'label': 'Industri', 'value': 'Kondisi Wilayah Sekitar_Industri'},
            {'label': 'Komersial', 'value': 'Kondisi Wilayah Sekitar_Komersial'},
        #    {'label': 'Pemerintahan', 'value': 'Kondisi Wilayah Sekitar_Pemerintahan'},
            {'label': 'Perumahan', 'value': 'Kondisi Wilayah Sekitar_Perumahan'},
        ],
        placeholder='Select Kondisi Wilayah Sekitar'
    ),
    dcc.Dropdown(
        id='kondisi-tapak-dropdown',
        options=[
            {'label': 'Darat / Kering', 'value': 'Kondisi Tapak_Darat / Kering'},
            {'label': 'Tanah Mentah', 'value': 'Kondisi Tapak_Tanah Mentah'},
       #     {'label': 'Tanah Rawa', 'value': 'Kondisi Tapak_Tanah Rawa'},
            {'label': 'Tanah Siap Dikembangkan (Tanah Matang)', 'value': 'Kondisi Tapak_Tanah Siap Dikembangkan (Tanah Matang)'},
        #    {'label': 'Tanah dalam Pengembangan', 'value': 'Kondisi Tapak_Tanah dalam Pengembangan'},
        ],
        placeholder='Select Kondisi Tapak'
    ),
    html.Button('Predict', id='predict-button', n_clicks=0),
    html.Div(id='output-predictions4')
])


####################### CALLBACKS ################################
@callback(
    Output('output-predictions4', 'children'),
    [Input('predict-button', 'n_clicks')],
    [State('lt-input', 'value'),
     State('air-label-dropdown', 'value'),
     State('listrik-label-dropdown', 'value'),
     State('distance-input', 'value'),
     State('lebar-jalan-input', 'value'),
     State('clusters-dropdown', 'value'),
     State('peruntukan-dropdown', 'value'),
     State('hap-dropdown', 'value'),
     State('kota-kabupaten-dropdown', 'value'),
     State('bentuk-tapak-dropdown', 'value'),
     State('kondisi-wilayah-dropdown', 'value'),
     State('kondisi-tapak-dropdown', 'value')]
)
def update_prediction(n_clicks, lt_input, air_label_input, listrik_label_input, distance_input, lebar_jalan_input, clusters, peruntukan, hap, kota_kabupaten, bentuk_tapak, kondisi_wilayah, kondisi_tapak):
    if n_clicks == 0 or None in [lt_input, air_label_input, listrik_label_input, distance_input, lebar_jalan_input, clusters, peruntukan, hap, kota_kabupaten, bentuk_tapak, kondisi_wilayah, kondisi_tapak]:
        return None

    user_input = [
        float(lt_input),
        int(air_label_input),
        int(listrik_label_input),
        float(distance_input),
        float(lebar_jalan_input),
        clusters,
        peruntukan,
        hap,
        kota_kabupaten,
        bentuk_tapak,
        kondisi_wilayah,
        kondisi_tapak
    ]

    prediction = make_predictions(loaded_scaler,loaded_model, user_input)

    return html.Div([
        html.H2("Prediction:"),
        html.H4(f"{prediction}")
    ])





def make_predictions(scaler, model, new_data):
    # Define all feature names used during training
    all_features = ['LT (m2)', 'Air_Label', 'Listrik_Label', 'Distance_Category_Label', 'Lebar Jalan Depan (m)']
    all_features += [f'Clusters_{i}' for i in range(4)]
    all_features += ['Peruntukan_Fasilitas Umum', 'Peruntukan_Kawasan Industri',
                     'Peruntukan_Kawasan Perdagangan dan Jasa', 'Peruntukan_Kawasan Peruntukan Perkebunan',
                     'Peruntukan_Pemukiman Perkotaan']
    all_features += ['Hak Atas Properti_AJB', 'Hak Atas Properti_Girik', 'Hak Atas Properti_HGB diatas HPL',
                     'Hak Atas Properti_HP', 'Hak Atas Properti_PPJB', 'Hak Atas Properti_SHGB',
                     'Hak Atas Properti_SHM', 'Hak Atas Properti_SHMSRS ', 'Hak Atas Properti_SIPPT']
    all_features += ['Kota/Kabupaten_Kabupaten Bandung',
       'Kota/Kabupaten_Kabupaten Bandung Barat',
       'Kota/Kabupaten_Kabupaten Bekasi',
        'Kota/Kabupaten_Kabupaten Bogor',
       'Kota/Kabupaten_Kabupaten Ciamis', 
    'Kota/Kabupaten_Kabupaten Cianjur',
       'Kota/Kabupaten_Kabupaten Cirebon', 
        'Kota/Kabupaten_Kabupaten Garut',
       'Kota/Kabupaten_Kabupaten Indramayu',
       'Kota/Kabupaten_Kabupaten Karawang',
       'Kota/Kabupaten_Kabupaten Kuningan',
       'Kota/Kabupaten_Kabupaten Majalengka',
       'Kota/Kabupaten_Kabupaten Pangandaran',
       'Kota/Kabupaten_Kabupaten Purwakarta',
       'Kota/Kabupaten_Kabupaten Subang', 
        'Kota/Kabupaten_Kabupaten Sukabumi',
       'Kota/Kabupaten_Kabupaten Sumedang',
       'Kota/Kabupaten_Kabupaten Tasikmalaya', 
        'Kota/Kabupaten_Kota Bandung',
       'Kota/Kabupaten_Kota Banjar', 
        'Kota/Kabupaten_Kota Bekasi',
       'Kota/Kabupaten_Kota Bogor',
        'Kota/Kabupaten_Kota Cimahi',
       'Kota/Kabupaten_Kota Cirebon',
        'Kota/Kabupaten_Kota Depok',
       'Kota/Kabupaten_Kota Sukabumi', 
        'Kota/Kabupaten_Kota Tasikmalaya']
    all_features += [ 'Bentuk Tapak_Kipas', 
        'Bentuk Tapak_Letter L', 
        'Bentuk Tapak_Ngantong',
       'Bentuk Tapak_Persegi', 
        'Bentuk Tapak_Persegi Panjang',
       'Bentuk Tapak_Tidak Beraturan', 
            'Bentuk Tapak_Trapesium']
    all_features += ['Kondisi Wilayah Sekitar_Campuran', 'Kondisi Wilayah Sekitar_Hijau',
                     'Kondisi Wilayah Sekitar_Industri', 'Kondisi Wilayah Sekitar_Komersial',
                     'Kondisi Wilayah Sekitar_Perumahan']
    all_features += ['Kondisi Tapak_Darat / Kering', 'Kondisi Tapak_Tanah Mentah', 
                     'Kondisi Tapak_Tanah Siap Dikembangkan (Tanah Matang)']

    # Initialize input data list with zeros for all features
    input_data = [0] * len(all_features)

    # Update input data with user's selections
    lt, air_label, listrik_label, distance_category, lebar_jalan, cluster, peruntukan, hap, kota_kabupaten, bentuk_tapak, kondisi_wilayah, kondisi_tapak = new_data
    input_data[all_features.index('LT (m2)')] = lt
    input_data[all_features.index('Air_Label')] = air_label
    input_data[all_features.index('Listrik_Label')] = listrik_label
    input_data[all_features.index('Distance_Category_Label')] = distance_category
    input_data[all_features.index('Lebar Jalan Depan (m)')] = lebar_jalan
    input_data[all_features.index(f'Clusters_{cluster}')] = 1
    input_data[all_features.index(peruntukan)] = 1
    input_data[all_features.index(hap)] = 1
    input_data[all_features.index(kota_kabupaten)] = 1
    input_data[all_features.index(bentuk_tapak)] = 1
    input_data[all_features.index(kondisi_wilayah)] = 1
    input_data[all_features.index(kondisi_tapak)] = 1

    # Scale the input data
    scaled_input_data = scaler.transform([input_data])

    # Make predictions using the loaded model
    prediction = model.predict(scaled_input_data)
    # Format the prediction with commas between numbers
    formatted_prediction = "{:,.2f} Juta Rupiah".format(prediction[0])

    return formatted_prediction