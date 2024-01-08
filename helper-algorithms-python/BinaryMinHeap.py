# Heap inicializálása üres listaként
heap = []

# Elem beszúrása a heap-be
def insert_into_heap(heap, element):
    heap.append(element)  # Hozzáadjuk az elemet a heap végére
    # Az elemet felfelé mozgatjuk, hogy visszaállítsuk a heap tulajdonságokat
    index = len(heap) - 1
    while index > 0:
        parent_index = (index - 1) // 2
        if heap[parent_index] > heap[index]:
            # Ha az elem kisebb, mint a szülője, akkor cseréljük azokat
            heap[parent_index], heap[index] = heap[index], heap[parent_index]
            index = parent_index
        else:
            break

# Minimum elem törlése a heap-ből
def delete_min_from_heap(heap):
    if not heap:
        return None  # Ha a heap üres, nincs mit törölni

    # A minimum elem a heap elején található
    min_element = heap[0]

    # Az utolsó elemet áthelyezzük az első pozícióba
    heap[0] = heap[-1]
    heap.pop()  # Töröljük az utolsó elemet
    index = 0

    # Az elemet lefelé mozgatjuk, hogy helyreállítsuk a heap tulajdonságokat - heapify
    while True:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        # Kiválasztjuk a két gyermek közül a kisebbet
        if left_child_index < len(heap) and heap[left_child_index] < heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(heap) and heap[right_child_index] < heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            # Ha a gyermek kisebb, mint az elem, cseréljük őket
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break

    return min_element

# Elemek beszúrása a heap-be
insert_into_heap(heap, 5)
insert_into_heap(heap, 3)
insert_into_heap(heap, 8)
insert_into_heap(heap, 1)
insert_into_heap(heap, 10)

print("Heap tartalma:", heap)

# Minimum elem törlése a heap-ből
min_element = delete_min_from_heap(heap)
print("Törölt minimum elem:", min_element)
print("Heap tartalma a törlés után:", heap)
