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




# Pedir las ciudades al usuario
print("Ingrese el nombre tal cual como se muestra en la pantalla")
print(" ")
print("Las ciudades son:")
print("---------------------------------------------------------------------")
print("Madrid, Barcelona, Paris, Brussels, Amsterdam, Berlin, Prague, Vienna")
print("Budapest, Rome, Lisbon, London, Dublin, Milan, Zurich, Wasaw")
print("Naples, Belgrade, Sofia, Bucharest, Krakow")
print("---------------------------------------------------------------------")
ciudad_origen = input("Ingrese la ciudad de origen: ")
ciudad_destino = input("Ingrese la ciudad de destino: ")

# Encontrar la ruta más corta entre las dos ciudades ingresadas por el usuario
distance, path = dijkstra(graph, ciudad_origen, ciudad_destino)
print("Distancia total:", distance)
print("Ruta más corta:", path)