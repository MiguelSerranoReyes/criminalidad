import dash
from dash import dcc, html 
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


app = dash.Dash(__name__)

opciones_delitos = [
    'DELITO DE BAJO IMPACTO',
    'ROBO A TRANSEUNTE EN VÍA PÚBLICA CON Y SIN VIOLENCIA',
    'ROBO DE VEHÍCULO CON Y SIN VIOLENCIA',
    'LESIONES DOLOSAS POR DISPARO DE ARMA DE FUEGO',
    'HECHO NO DELICTIVO',
    'VIOLACIÓN',
    'ROBO A NEGOCIO CON VIOLENCIA',
    'ROBO A REPARTIDOR CON Y SIN VIOLENCIA',
    'ROBO A PASAJERO A BORDO DE MICROBUS CON Y SIN VIOLENCIA',
    'HOMICIDIO DOLOSO',
    'ROBO A PASAJERO A BORDO DEL METRO CON Y SIN VIOLENCIA',
    'ROBO A PASAJERO A BORDO DE TAXI CON VIOLENCIA',
    'ROBO A CUENTAHABIENTE SALIENDO DEL CAJERO CON VIOLENCIA',
    'ROBO A CASA HABITACIÓN CON VIOLENCIA',
    'ROBO A TRANSPORTISTA CON Y SIN VIOLENCIA',
    'SECUESTRO'
]

# Cargar los datos
df = pd.read_csv('carpetasFGJ_2023.csv')  # Asegúrate de que el nombre del archivo sea correcto

# Filtrar para asegurar que todas las filas tengan coordenadas
df = df.dropna(subset=['latitud', 'longitud'])

# Definir el layout de la aplicación
app.layout = html.Div([
    html.H1("Mapa de Calor de Criminalidad en la Ciudad de México", className='h1'),
    dcc.Dropdown(
        id='mi-dropdown',
        options=[{'label': delito, 'value': delito} for delito in opciones_delitos],
        value='DELITO DE BAJO IMPACTO'
    ),
    html.Div(id='mi-output', style={'marginTop': 20}),
    dcc.Graph(id='mi-grafico', className='graph')
], className='body')

# Callback para actualizar el contenido y el estilo del fondo según la selección del usuario
@app.callback(
    Output('mi-grafico', 'figure'),
    [Input('mi-dropdown', 'value')]
)
def actualizar_grafico(delito_seleccionado):
    df_filtrado = df[df['categoria'] == delito_seleccionado]
    
    # Crear la figura del mapa de calor
    fig = px.density_mapbox(df_filtrado, lat='latitud', lon='longitud', 
                            radius=10, 
                            center={"lat": 19.36, "lon": -99.133209},  # Centro en la Ciudad de México
                            zoom=10, 
                            mapbox_style="mapbox://styles/mapbox/light-v10")  # Puedes cambiar el estilo del mapa aquí

    fig.update_layout(mapbox_accesstoken='token')

    return fig


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)