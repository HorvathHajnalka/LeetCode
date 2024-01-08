def typetime(keyboard, s):
    def binary_search(arr, target): # O(logN)
        #eloszor a ket index a tomb ket szele 
        left = 0
        right = len(arr) - 1
        while left <= right: #amig a bal index < jobb index
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid  # A keresett elem indexe
            elif arr[mid] < target: #ha a kozepen levo elem kisebb,mint a cel, akkor elorebb toljuk az indexelest
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Ha az elem nincs a listában

    current = 0
    move = 0
    idx = 0
    for c in s: # O(s*logn), ahol s a keresett szó hossza
        idx = binary_search(keyboard,c)
        move += abs(current - idx)
        current = idx
    return move
    
print(typetime("abcdefghijklmnopqrstuvwxyz", "cba" ))