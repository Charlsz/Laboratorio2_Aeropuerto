import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from funcionamiento import dijkstra

# Definir el grafo con las conexiones entre las ciudades y sus distancias
graph = {}
with open("grafo_europa.txt") as file:
    for line in file:
        city1, city2, distance = line.strip().split(",")
        distance = int(distance)
        if city1 not in graph:
            graph[city1] = []
        if city2 not in graph:
            graph[city2] = []
        graph[city1].append((city2, distance))
        graph[city2].append((city1, distance))

# Definir la aplicación Dash
app = dash.Dash(__name__)

# Definir el contenido HTML de la aplicación
app.layout = html.Div([
    html.H1('Calculadora de Rutas Europeas'),
    html.P('Ingrese la ciudad de origen y destino para encontrar la ruta más corta entre ellas:'),
    dcc.Dropdown(
        id='ciudad_origen',
        options=[{'label': city, 'value': city} for city in graph.keys()],
        placeholder='Ciudad de origen'
    ),
    dcc.Dropdown(
        id='ciudad_destino',
        options=[{'label': city, 'value': city} for city in graph.keys()],
        placeholder='Ciudad de destino'
    ),
    html.Button('Calcular Ruta', id='calcular-ruta', n_clicks=0),
    html.Br(),
    html.Br(),
    html.Div(id='output')
])

# Definir la función que se ejecuta al hacer clic en el botón de calcular ruta
@app.callback(
    Output('output', 'children'),
    Input('calcular-ruta', 'n_clicks'),
    Input('ciudad_origen', 'value'),
    Input('ciudad_destino', 'value')
)
def calcular_ruta(n_clicks, ciudad_origen, ciudad_destino):
    if n_clicks > 0 and ciudad_origen is not None and ciudad_destino is not None:
        # Encontrar la ruta más corta entre las dos ciudades ingresadas por el usuario
        distance, path = dijkstra(graph, ciudad_origen, ciudad_destino)
        return html.Div([
            html.P('Distancia total: {}'.format(distance)),
            html.P('Ruta más corta: {}'.format(', '.join(path)))
        ])
    else:
        return html.P('Por favor, ingrese una ciudad de origen y una ciudad de destino y haga clic en "Calcular Ruta".')

if __name__ == '__main__':
    app.run_server(debug=True)
