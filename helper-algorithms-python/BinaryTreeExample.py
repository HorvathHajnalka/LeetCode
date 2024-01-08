class Node:
    def __init__(self, key):
        self.left = None  # Bal oldali részfa
        self.right = None  # Jobb oldali részfa
        self.value = key  # A csomópont értéke
# elem megtalálása
 while root:
    if root.val == val:
        return root
    if root.val > val:
        root = root.left
    else:
        root = root.right


def insert(root, key):
    if root is None:
        return Node(key)  # Új csomópont létrehozása, ha a fa üres
    else:
        if key < root.value:
            root.left = insert(root.left, key)  # Szúrás a bal oldalon
        else:
            root.right = insert(root.right, key)  # Szúrás a jobb oldalon
    return root

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = deleteNode(root.left, key)  # Törlés a bal oldalon
    elif key > root.value:
        root.right = deleteNode(root.right, key)  # Törlés a jobb oldalon
    else: # megtaláltuk az elemet
        if root.left is None: #ha nincs gyereke /csak 1 ->atallitjuk a mutatot
            return root.right  # Nincs bal részfa ->  az eredeti elemet eltávolítjuk, és az új gyökér elem a korábbi jobb részfa gyökere lesz.
        elif root.right is None:
            return root.left  # Nincs jobb részfa
        #ha 2 gyereke van
        root.value = minValueNode(root.right).value  # Az utód értékének átmásolása, legkisebb érték megy a torlendo helyére
        root.right = deleteNode(root.right, root.value)  # Az utód eltávolítása
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")  # Inorder bejárás, értékek kiírása
        inorder_traversal(root.right)

# Példa a bináris fa működésére
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Bináris fa inorder bejárása:")
inorder_traversal(root)

key_to_delete = 30
root = deleteNode(root, key_to_delete)
print(f"\nA(z) {key_to_delete} elemet törölve:")
inorder_traversal(root)
