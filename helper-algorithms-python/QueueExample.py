
# Elemek hozzáadása a sorhoz
def enqueue(queue, item):
    queue.append(item)

# Ellenőrzés, hogy a sor üres-e
def is_empty(queue):
    return len(queue) == 0

# A sor elején lévő elem lekérése
def peek(queue):
    if not is_empty(queue):
        return queue[0]
    else:
        return None

# Elem eltávolítása a sorból
def dequeue(queue):
    if not is_empty(queue):
        return queue.pop(0)
    else:
        return None

# A sor kiürítése
def clear_queue(queue):
    queue.clear()

# Sor létrehozása
my_queue = []

# Elemek hozzáadása a sorhoz
enqueue(my_queue, 1)
enqueue(my_queue, 2)
enqueue(my_queue, 3)

# A sor elején lévő elem lekérése
print("Sor elején lévő elem:", peek(my_queue))

# Elem eltávolítása a sorból és kiíratása
print("Eltávolított elem:", dequeue(my_queue))

# Ellenőrzés, hogy a sor üres-e
print("A sor üres?", is_empty(my_queue))

# A sor kiürítése
clear_queue(my_queue)

# Ellenőrzés, hogy a sor üres-e kiürítés után
print("A sor üres kiürítés után?", is_empty(my_queue))
