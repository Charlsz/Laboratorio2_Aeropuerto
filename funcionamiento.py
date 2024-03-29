import heapq
from collections import deque

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

def obtener_grafo():
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

    return graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for neighbor, _ in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for neighbor, _ in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)






#ciudad_origen = input("Ingrese la ciudad de origen: ")
#ciudad_destino = input("Ingrese la ciudad de destino: ")

# Encontrar la ruta más corta entre las dos ciudades ingresadas por el usuario
#distance, path = dijkstra(graph, ciudad_origen, ciudad_destino)
#print("Distancia total:", distance)
#print("Ruta más corta:", path)
#print("")
#print("")
# Realizar un recorrido BFS empezando por Madrid
#graph = obtener_grafo()
#print("RECORRIDO BFS-----------------------------------")
#bfs(graph, "Madrid")
#print(" ")
# Realizar un recorrido DFS empezando por Madrid
#print("RECORRIDO DFS-----------------------------------")
#dfs(graph, "Madrid")