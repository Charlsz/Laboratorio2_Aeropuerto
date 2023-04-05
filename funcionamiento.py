import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    path = {}
    visited = set()

    while queue:
        (current_distance, current_vertex) = heapq.heappop(queue)

        if current_vertex == end:
            return (distances[current_vertex], construct_path(path, start, end))

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    return float("inf"), []

def construct_path(path, start, end):
    result = [end]
    current = end

    while current != start:
        current = path[current]
        result.append(current)

    result.reverse()
    return result

# Definir el grafo con las conexiones entre las ciudades y sus distancias
graph = {
    "Madrid": [("Lisbon", 635), ("Paris", 1056), ("Barcelona", 621)],
    "Barcelona": [("Madrid", 621), ("Paris", 831), ("Milan", 862), ("Lisbon", 1204)],
    "Paris": [("Madrid", 1056), ("Barcelona", 831), ("Brussels", 265), ("Amsterdam", 430), ("Berlin", 878), ("Rome", 1105)],
    "Brussels": [("Paris", 265), ("Amsterdam", 173), ("Berlin", 655), ("London", 321)],
    "Amsterdam": [("Paris", 430), ("Brussels", 173), ("Berlin", 663), ("London", 358)],
    "Berlin": [("Paris", 878), ("Brussels", 655), ("Amsterdam", 663), ("Prague", 280), ("Vienna", 665), ("Warsaw", 574)],
    "Prague": [("Berlin", 280), ("Vienna", 330), ("Budapest", 530), ("Krakow", 537)],
    "Vienna": [("Berlin", 665), ("Prague", 330), ("Budapest", 243), ("Rome", 1036)],
    "Budapest": [("Prague", 530), ("Vienna", 243), ("Belgrade", 370), ("Sofia", 472), ("Bucharest", 605)],
    "Rome": [("Paris", 1105), ("Vienna", 1036), ("Naples", 225)],
    "Lisbon": [("Madrid", 635), ("Barcelona", 1204)],
    "London": [("Brussels", 321), ("Amsterdam", 358), ("Dublin", 463)],
    "Dublin": [("London", 463)],
    "Milan": [("Barcelona", 862), ("Zurich", 222), ("Vienna", 719)],
    "Zurich": [("Milan", 222), ("Vienna", 672)],
    "Warsaw":[("Berlin",574)],
    "Naples":[("Rome",225)],
    "Belgrade": [("Budapest",370)],
    "Sofia": [("Budapest",472)],
    "Bucharest": [("Budapest",605)],
    "Krakow": [("Prague",537)]
}



# Pedir las ciudades al usuario
ciudad_origen = input("Ingrese la ciudad de origen: ")
ciudad_destino = input("Ingrese la ciudad de destino: ")

# Encontrar la ruta más corta entre las dos ciudades ingresadas por el usuario
distance, path = dijkstra(graph, ciudad_origen, ciudad_destino)
print("Distancia total:", distance)
print("Ruta más corta:", path)