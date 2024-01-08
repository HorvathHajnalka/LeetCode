#  egyszerre keres a kezdeti és a végállapot felé, hogy csökkentse a keresési teret és javítsa a keresés hatékonyságát
def bidirectional_search(graph, start, end):
    if start == end:
        return [start]  # Ha a kezdeti és a végpont ugyanaz, rögtön visszatérünk a kezdeti ponttal

    # Kezdeti és végpontok előremenő és hátrafelé tartó kezdeti sorai
    forward_queue = [(start, [start])] # Minden elem egy tuple, ahol az első elem a jelenleg vizsgált csúcs, a második pedig az útvonal, amely az adott csúcsig vezet.
    backward_queue = [(end, [end])]

    # A már feldolgozott csúcsok halmazai
    forward_visited = []
    backward_visited = []

    while forward_queue and backward_queue:
        # Előremenő keresés egy lépést tesz
        current, path = forward_queue.pop(0) # kivesszük a listából
        forward_visited.append(current) # már meglátogattuk
        for neighbor in graph[current]: #végigmegyünk az elem kapcsolatain 
            if neighbor not in forward_visited: #ha van olyan kapcsolat amit még nem látogattunk
                new_path = path + [neighbor]
                forward_queue.append((neighbor, new_path))

                # Ellenőrizzük, hogy a végpontot elértük-e a hátrafelé keresés során
                if neighbor in backward_visited: #ha van olyan elem amit visszafele már néztünk
                    intersection = neighbor # metszet beállítása
                    #visszaadja az utat
                    forward_path = new_path 
                    backward_path_index = backward_visited.index(neighbor)
                    backward_path = backward_visited[backward_path_index:]
                    backward_path = list(reversed(backward_path))  # Visszaadja az utat
                    return forward_path + backward_path

        # Hátrafelőre keresés egy lépést tesz
        current, path = backward_queue.pop(0)
        backward_visited.append(current)

        for neighbor in graph[current]:
            if neighbor not in backward_visited:
                new_path = [neighbor] + path
                backward_queue.append((neighbor, new_path))

    return None  # Ha nincs út a kezdeti és végpont között

# Példa gráf definiálása - szótár, kulcs = node, érték = edge-k
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

start_node = "A"
end_node = "G"

result = bidirectional_search(graph, start_node, end_node)

if result:
    print("Bidirectional search útvonal:")
    print(" -> ".join(result))
else:
    print("Nincs út a kezdeti és végpont között.")
