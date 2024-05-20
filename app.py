import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats as st
import scipy.stats
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Reemplaza los valores ausentes de is_4wd y paint_color por un valor definido
car_data['is_4wd'] = car_data['is_4wd'].fillna(value= 0)
car_data['paint_color'] = car_data['paint_color'].fillna(value='Unknown')

# Calcula la mediana de model_year para cada model
model_year_means = car_data.groupby('model')['model_year'].median()

# Define una función para reemplazar los valores ausentes con la mediana correspondiente
def fill_missing_model_year(row):
    if pd.isna(row['model_year']):
        return model_year_means[row['model']]
    else:
        return row['model_year']

# Aplica la función a cada fila del DataFrame
car_data['model_year'] = car_data.apply(fill_missing_model_year, axis=1)

# Calcula el promedio de cylinders  para cada model
model_year_means = car_data.groupby('model')['cylinders'].mean()

# Define una función para reemplazar los valores ausentes con el promedio correspondiente
def fill_missing_cylinders(row):
    if pd.isna(row['cylinders']):
        return model_year_means[row['model']]
    else:
        return row['cylinders']

# Aplica la función a cada fila del DataFrame
car_data['cylinders'] = car_data.apply(fill_missing_cylinders, axis=1)

# Calcula el promedio de 'odometer' para cada 'model' y redondear a dos decimales
model_odometer_means = car_data.groupby('model')['odometer'].mean().round(2)

# Función para rellenar valores ausentes en 'odometer' con el promedio del modelo
def fill_missing_odometer(row):
    if pd.isna(row['odometer']):
        return model_odometer_means[row['model']]
    else:
        return row['odometer']

# Aplica la función a cada fila del DataFrame
car_data['odometer'] = car_data.apply(fill_missing_odometer, axis=1)

car_data['odometer'] = car_data['odometer'].fillna(value= 500000) #Remmplazar con un valor fijo ya que un modelo completo no se diligencio el cuentakilómetros
print(car_data[car_data['odometer'].isna()])

# Crea una nueva columna que nos permita analizar si el vehiculo esta en optimas condiciones de acuerdo al kilometraje y su antiguadad

# Convierte 'date_posted' a formato de fecha
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'], errors='coerce')

# Extrae el año de 'date_posted'
car_data['year_posted'] = car_data['date_posted'].dt.year

# Crea una nueva columna que calcule la diferencia en años entre 'date_posted' y 'model_year'
car_data['age_at_posting'] = car_data['year_posted'] - car_data['model_year']

# Convierte a entero varias columnas para posteriores calculos
car_data['age_at_posting'] = car_data['age_at_posting'].astype(int)
car_data['cylinders'] = car_data['cylinders'].astype(int)
car_data['model_year'] = car_data['model_year'].astype(int)
car_data['odometer'] = car_data['odometer'].astype(int)

# Extrae la marca de carro de la columna 'model'
car_data['brand'] = car_data['model'].str.split().str[0]

# Nueva tabla para poder crear un grafico de dispersión que pueda analizar de acuerdo a la condicion el promedio precio y kilometraje
analysis_condition = car_data.groupby(['model_year','condition']).agg({'price':'mean', 'odometer':'mean'}).reset_index()


st.header('Gráficos de Análisis de Precios de Vehículos en EE.UU.') # encabezado de la app

checkbox_hist = st.checkbox("Histograma")

if checkbox_hist: # al hacer clic en el checkbox
    
    # Calcular el precio promedio de acuerdo a odometer y brand
    avg_price_by_odometer_brand = car_data.groupby(['brand', 'odometer']).agg({'price': 'mean'}).reset_index() 
    # Crear el histograma
    fig1 = px.histogram(avg_price_by_odometer_brand, x='odometer', y='price', color='brand', barmode='group', title='Precio Promedio según Kilometraje y Marca', labels={'odometer': 'Kilometraje', 'price': 'Precio Promedio', 'brand': 'Marca'})
    st.plotly_chart(fig1, use_container_width=True)
    
checkbox_scatt = st.checkbox("Dispersión")

if checkbox_scatt: # al hacer clic en el checkbox
    # Crear el gráfico de dispersion agrupado por la condicion y con el tamaño por kilometraje
    fig2 = px.scatter(analysis_condition, x='model_year', y='price', size='odometer',color='condition', title='Precio de vehiculo de acuerdo al año y kilometraje de acuerdo a su condición')
    st.plotly_chart(fig2, use_container_width=True)
