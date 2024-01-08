#rendezett tombon
def binary_search(arr, target):
    #eloszor a ket index a tomb ket szele 
    left, right = 0, len(arr) - 1
    while left <= right: #amig a bal index < jobb index
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # A keresett elem indexe
        elif arr[mid] < target: #ha a kozepen levo elem kisebb,mint a cel, akkor elorebb toljuk az indexelest
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Ha az elem nincs a listában

# Példa a használatra
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"A keresett elem ({target}) az indexen {result} található.")
else:
    print(f"A keresett elem ({target}) nem található a listában.")
