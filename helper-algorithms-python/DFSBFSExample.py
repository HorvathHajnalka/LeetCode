class Graph:
    def __init__(self):
        # Inicializáljuk a gráfot egy üres szótárral, ahol a kulcsok a csúcsok és az értékek azokhoz kapcsolódó szomszédok lesznek.
        self.graph = {}

    def add_edge(self, start, end):
        # Hozzáadjuk az élt a gráfhoz. Ha a kezdő csúcs már szerepel a gráfban, csak hozzáadjuk az újabb szomszédot, egyébként létrehozunk egy új kulcsot.
        if start in self.graph:
            self.graph[start].append(end)
        else:
            self.graph[start] = [end]

    #mielőtt mélyebb szintre mennénk mindig megnézzük a szomszédos elemeket
    def breadth_first_search(self, start):
        visited = set()  # Ebben a halmazban tároljuk a meglátogatott csúcsokat.
        queue = [start]  # A BFS sor.
        result = []  # Ebben a listában tároljuk a megtalált csúcsok sorrendjét.

        while queue:
            node = queue.pop(0)  # Kivesszük a sorból az első csúcsot.
            if node not in visited:
                visited.add(node)  # Megjelöljük a csúcsot meglátogatottként.
                result.append(node)  # Hozzáadjuk a csúcsot a talált sorhoz.
                # Az összes szomszédot hozzáadjuk a sorhoz, amelyek még nem lettek meglátogatva.
                queue.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited) #mivel mindig törlünk aztán bővítünk, ha végigér a szomszédokon szintet lép

        return result

    #mielőtt a szomszédos elemhez ugranánk, a mélyéig elmegyünk a kapcsolatoknak
    def depth_first_search(self, start):
        def dfs(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Rekurzívan meghívjuk a dfs függvényt minden szomszédra, amelyek még nem lettek meglátogatva.
                for neighbor in self.graph.get(node, []): # megpróbálja visszaadni a node kulcshoz tartozó értéket (azaz a szomszédok listáját)
                    if neighbor not in visited:
                        dfs(neighbor) #ha mindig a szomszédra hívjuk mélyebbre megy

        visited = set()  # Ebben a halmazban tároljuk a meglátogatott csúcsokat.
        result = []  # Ebben a listában tároljuk a megtalált csúcsok sorrendjét.
        dfs(start)  # Elindítjuk a mélységi keresést a kezdőcsúccsal.
        return result

# Példa gráf definiálása
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('E', 'F')
graph.add_edge('F', 'G')

# Szélességi keresés
print("Breadth-First Search:")
bfs_result = graph.breadth_first_search('A')
print(bfs_result)

# Mélységi keresés
print("Depth-First Search:")
dfs_result = graph.depth_first_search('A')
print(dfs_result)

#------------------------------------------------------------------------------------------------------------ BINÁRIS FÁKRA
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

def dfs_preorder(root):
    if not root:
        return []

    result = []
    result.append(root.value)
    result += dfs_preorder(root.left)
    result += dfs_preorder(root.right)

    return result

def dfs_inorder(root):
    if not root:
        return []

    result = []
    result += dfs_inorder(root.left)
    result.append(root.value)
    result += dfs_inorder(root.right)

    return result

def dfs_postorder(root):
    if not root:
        return []

    result = []
    result += dfs_postorder(root.left)
    result += dfs_postorder(root.right)
    result.append(root.value)

    return result

# Példa fa felépítése
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# BFS bejárás
bfs_result = bfs(root)
print("BFS Bejárás:", bfs_result)

# DFS preorder bejárás
dfs_preorder_result = dfs_preorder(root)
print("DFS Preorder Bejárás:", dfs_preorder_result)

# DFS inorder bejárás
dfs_inorder_result = dfs_inorder(root)
print("DFS Inorder Bejárás:", dfs_inorder_result)

# DFS postorder bejárás
dfs_postorder_result = dfs_postorder(root)
print("DFS Postorder Bejárás:", dfs_postorder_result)
