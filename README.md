# Laboratorio2_Aeropuerto

El siguiente código incluye funciones para calcular la ruta más corta entre dos nodos en un grafo, realizar un recorrido BFS (Breadth-First Search) y un recorrido DFS (Depth-First Search) del grafo a partir de un nodo dado. El código utiliza el algoritmo de Dijkstra para calcular la ruta más corta.

Para utilizar estas funciones, primero se debe crear un grafo en formato de diccionario de adyacencia. El archivo "grafo_europa.txt" contiene las conexiones entre ciudades de Europa y sus distancias. La función "obtener_grafo()" lee este archivo y devuelve el grafo como un diccionario.

Funciones:

dijkstra(graph, start, end):
Calcula la ruta más corta entre los nodos 'start' y 'end' en el grafo utilizando el algoritmo de Dijkstra. Recibe como parámetros el grafo, el nodo de inicio y el nodo de fin. Devuelve una tupla con la distancia más corta y la ruta que se debe seguir para llegar del nodo 'start' al nodo 'end'.

construct_path(path, start, end):
Construye la ruta de nodos que se debe seguir para llegar del nodo 'start' al nodo 'end' a partir de un diccionario 'path' que contiene los nodos precedentes de cada nodo en el camino más corto.

obtener_grafo():
Lee el archivo "grafo_europa.txt" y devuelve el grafo como un diccionario de adyacencia.

bfs(graph, start):
Realiza un recorrido BFS (Breadth-First Search) del grafo a partir del nodo 'start'. Recibe como parámetros el grafo y el nodo de inicio. Devuelve una lista que contiene el recorrido BFS del grafo a partir del nodo 'start'.

dfs(graph, start):
Realiza un recorrido DFS (Depth-First Search) del grafo a partir del nodo 'start'. Recibe como parámetros el grafo y el nodo de inicio. Devuelve una lista que contiene el recorrido DFS del grafo a partir del nodo 'start'.

Para utilizar estas funciones, se debe importar la librería heapq y la clase deque del módulo collections. También se debe llamar a la función "obtener_grafo()" para obtener el grafo en formato de diccionario de adyacencia.