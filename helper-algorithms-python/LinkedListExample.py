# A láncolt lista egy csomagoló osztály
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Láncolt lista inicializálása
"""ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}"""
class LinkedList:
    def __init__(self):
        self.head = None

    # Elem hozzáadása a lista végéhez
    def append(self, data):
        new_node = Node(data)
        if not self.head: #ha nincs benne elem
            self.head = new_node #beállítjuk headnek
        else:
            current = self.head #headtől indulunk
            while current.next: #amíg találunk elemet a nexten továbbmegyünk
                current = current.next #a következő elem a current
            current.next = new_node # ha már nincs következő (null), a beszúrt elemre állítjuk

    # Elem hozzáadása a lista elejéhez
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head # headre allitjuk new mutatojat
        self.head = new_node # lista headje lesz a beszurt elem

    # Elem keresése a listában
    def find(self, data):
        current = self.head #headtől indulunk
        while current: #amíg nem érünk el nullig
            if current.data == data: #ha a mutató értéke megegyezik a keresett értékkel 
                return True
            current = current.next # mutató továbbléptetése
        return False #ha nem találta meg az elemet false-al tér vissza

    # Elem eltávolítása a listából
    def remove(self, data):
        if not self.head: #ha nincs láncolt lista
            return
        if self.head.data == data: #ha a sor első eleme az eltávolítandó
            self.head = self.head.next # az új head az az elem, amire a head mutat
            return
        current = self.head # headtől indulunk
        while current.next: # amíg van következő elem
            if current.next.data == data: # ha megtalálta - a következő elem lenne
                current.next = current.next.next #átállítja a mutatót a következő utáni elemre
                return
            current = current.next #ha nincs egyezés, lépteti a mutatót

    # Lista kiíratása
    def display(self):
        elements = [] 
        current = self.head #headtől indulunk
        while current: #amíg nem kapunk null értéket
            elements.append(current.data) #listába fűz
            current = current.next #lépteti a mutatót
        print(" -> ".join(map(str, elements)))

# Láncolt lista létrehozása
my_list = LinkedList()

# Elemek hozzáadása a lista végéhez
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Lista kiíratása
my_list.display()

# Elem hozzáadása a lista elejéhez
my_list.prepend(0)

# Lista kiíratása
my_list.display()

# Elem eltávolítása a listából
my_list.remove(2)

# Lista kiíratása
my_list.display()

# Elem keresése a listában
found = my_list.find(3)
if found:
    print("Az elem megtalálható a listában.")
else:
    print("Az elem nincs a listában.")

#reverse - leetcode
class Solution(object):
    def reverseList(self, head):
# Initialize prev pointer as NULL..
        prev = None
        # Initialize the curr pointer as the head...
        curr = head
        # Run a loop till curr points to NULL...
        while curr:
            # Initialize next pointer as the next pointer of curr...
            nextp = curr.next
            # Now assign the prev pointer to curr’s next pointer.
            curr.next = prev
            # Assign curr to prev, next to curr...
            prev = curr
            curr = nextp
        return prev       # Return the prev pointer to get the reverse linked list...
