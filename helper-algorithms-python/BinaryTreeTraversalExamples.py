class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Inorder bejárás: bal, közép, jobb
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Preorder bejárás: közép, bal, jobb
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Postorder bejárás: bal, jobb, közép
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Példa egy bináris fa létrehozására
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder bejárás:")
inorder_traversal(root)
print("\n")

print("Preorder bejárás:")
preorder_traversal(root)
print("\n")

print("Postorder bejárás:")
postorder_traversal(root)
