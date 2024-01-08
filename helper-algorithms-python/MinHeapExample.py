#heap = complete binary tree, each node smaller thenn its children, root = minimumelement

# Új elem beszúrása a min heap-be
def min_heap_insert(heap, item):
    heap.append(item) #végére fűzzük legjobboldalibb, legalsóbb elem
    index = len(heap) - 1 #megkapja az utolsó indexet
    parent = (index - 1) // 2 #szülő = index -1 osztva 2-vel lefele kerekítve
    while index > 0 and heap[index] < heap[parent]: #ha az elem kisebb mint a szülő
        heap[index], heap[parent] = heap[parent], heap[index] #csere
        index = parent #index mozgatása

# A legkisebb elem kivétele a min heap-ből
def extract_min(heap):
    if len(heap) == 0:
        return None
    min_element = heap[0] #gyökér a minimum
    last_element = heap.pop() #kivesszük az utolsó elemet
    heap[0] = last_element #gyökérrel csere
    min_heapify(heap, 0)
    return min_element

# Min heapify függvény - a heap tulajdonság fenntartása
def min_heapify(heap, i):
    left = 2 * i + 1 #bal gyerek index
    right = 2 * i + 2 #jobb gyerek index
    smallest = i #legkisebb elem
    # Bal és jobb gyermek ellenőrzése, hogy van-e kisebb elem
    if left < len(heap) and heap[left] < heap[smallest]: # ha bal elem létezik és kisebb mint a smallestben tárolt érték
        smallest = left
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right
    # Ha a legkisebb elem nem a jelenlegi csúcs, cseréljük meg
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(heap, smallest)

# Min heap építése egy adott listából -- ?
def build_min_heap(arr):
 
    # Először a középtől kezdünk visszafelé, mivel az alsó szinteken található elemek már min heap-ek.
    for i in range(len(arr) // 2, -1, -1): # for(i=len(arr)//2 ; i>-1; i--)
        # Minden cikluslépésben megpróbáljuk biztosítani, hogy az i. elem és al-fája a min heap tulajdonságoknak megfeleljen.
        # Meghívjuk a min_heapify függvényt, hogy ellenőrizze és szükség esetén módosítsa az i. elem pozícióját.
        min_heapify(arr, i)




# Üres min heap létrehozása
min_heap = []

# Elemek hozzáadása a min heaphoz a függvény segítségével
min_heap_insert(min_heap, 4)
min_heap_insert(min_heap, 2)
min_heap_insert(min_heap, 7)
min_heap_insert(min_heap, 1)

print("Min Heap elemei:", min_heap)

# A min heap legkisebb elemének kivétele
min_element = extract_min(min_heap)
print("Kivett legkisebb elem:", min_element)
print("Maradék Min Heap:", min_heap)
