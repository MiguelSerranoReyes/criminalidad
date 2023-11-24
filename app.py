import dash
from dash import dcc, html 
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('carpetasFGJ_2023.csv')  # Asegúrate de que el nombre del archivo sea correcto

# Filtrar para asegurar que todas las filas tengan coordenadas
df = df.dropna(subset=['latitud', 'longitud'])

# Crear la figura del mapa de calor
fig = px.density_mapbox(df, lat='latitud', lon='longitud', 
                        radius=10, 
                        center={"lat": 19.36, "lon": -99.133209},  # Centro en la Ciudad de México
                        zoom=10, 
                        mapbox_style="mapbox://styles/mapbox/light-v10")  # Puedes cambiar el estilo del mapa aquí

fig.update_layout(mapbox_accesstoken='tu_clave_aqui')

# Iniciar la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div([
    html.H1("Mapa de Calor de Criminalidad en la Ciudad de México", className='h1'),
    dcc.Graph(figure=fig, className='graph')
], className='body')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)