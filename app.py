import plotly.express as px
from dash import Dash, dcc, html, Input, Output

acciones = px.data.stocks()
EMPRESAS = ["GOOG", "AAPL", "AMZN", "FB", "NFLX", "MSFT"]

app = Dash(__name__)
server=app.server

app.layout = html.Div([
    html.H1("Acciones de tecnología"),
    dcc.Checklist(options=EMPRESAS, value=["GOOG", "AAPL"], inline=True, id="empresas"),
    dcc.RadioItems(options=["Todo", "2018", "2019"], value="Todo", inline=True, id="periodo"),
    html.H3(id="resumen"),                     # texto que se actualiza
    dcc.Graph(id="grafica"),
])

@app.callback(
    Output("grafica", "figure"),
    Output("resumen", "children"),
    Input("empresas", "value"),
    Input("periodo", "value"),
)
def actualizar(empresas, periodo):
    if not empresas:                            # si no marcaron nada, no hay nada que calcular
        return px.line(), "Marca al menos una empresa."

    datos = acciones
    if periodo != "Todo":
        datos = acciones[acciones["date"].str.startswith(periodo)]

    fig = px.line(datos, x="date", y=empresas)

    cambio = datos[empresas].iloc[-1] / datos[empresas].iloc[0] - 1    # último valor entre el primero
    bajo = cambio.idxmin()                                            # la empresa que más bajo
    return fig, f"La que bajó más del periodo: {bajo} ({cambio[bajo]:-.0%})"

if __name__ == "__main__":
    app.run(debug=True)



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
