
# Proyecto de Mapa de Calor de Criminalidad

Este proyecto es una aplicación web creada con Dash y Plotly para visualizar un mapa de calor de criminalidad en la Ciudad de México. Deberás descargar del sitio de datos abiertos de la CdMx el archivo .csv correspondiente que quieras visualizar [Carpetas de investigación FGJ](https://datos.cdmx.gob.mx/dataset/carpetas-de-investigacion-fgj-de-la-ciudad-de-mexico). En este ejemplo usamos los datos correspondientes a Carpetas de Investigación de la FGJ (2023).

## Configuración

Para comenzar, sigue estos pasos:

### 1. Clonar el Repositorio

Clona este repositorio a tu máquina local usando:

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para instalar las dependencias. Puedes crear uno usando:

```bash
python -m venv .venv
```

Activar el entorno virtual:

En Windows:
```bash
.venv\Scripts\activate
```

En MacOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Instalar Dependencias

Instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

### 4. Configurar Mapbox

Obtén una clave API de Mapbox (token) registrándote en [Mapbox](https://www.mapbox.com/). Asegúrate de no subir tu clave API a tu repositorio.

### 5. Ejecutar la Aplicación

Para ejecutar la aplicación, usa:

```bash
python app.py
```

## Uso

Abre tu navegador y dirígete a `http://127.0.0.1:8050/` para ver la aplicación.

## Contribuir

Para contribuir al proyecto, asegúrate de no subir tu entorno virtual o tu clave API de Mapbox.
