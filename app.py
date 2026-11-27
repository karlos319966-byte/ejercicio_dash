import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# 1. Usamos 'r' para evitar errores con las barras de Windows
ruta = r"C:\Users\fco04\Documents\metrobus\afluencia.csv"

# 2. Leemos el archivo CSV con pandas para tener la tabla de datos
metrobus = pd.read_csv(ruta)

# 3. Creamos la gráfica (ajustando X e Y según los nombres exactos de tus columnas)
fig = px.line(metrobus, x="linea", y=["afluencia"])

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Afluencia vs linea del metrobus"),
    dcc.Graph(figure=fig),
])

if __name__ == "__main__":
    app.run(debug=True)
