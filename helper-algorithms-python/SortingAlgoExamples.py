def quicksort(arr): 
    if len(arr) <= 1: # kiszurjuk, hogy 1/0 elemu a tomb
        return arr
    
    pivot = arr[len(arr) // 2] # felosztó elemet(pivot) választunk(általában a lista közepéről)
    left = [x for x in arr if x < pivot] # bal a pivotnál kisebb elemek
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] # jobb a pivotnál nagyobb elemek
    
    return quicksort(left) + middle + quicksort(right) # csoportosított részlisták rendezése

def mergesort(arr): #részekre osztjuk a tömböt->rendezzük -> összemergeljük
    if len(arr) <= 1: # kiszurjuk, hogy 1/0 elemu a tomb
        return arr
    
    middle = len(arr) // 2 # felosztóelem létrehozása
    left = arr[:middle] # eredeti lista első fele lesz a bal
    right = arr[middle:] # eredeti lista második fele lesz a jobb
    
    return merge(mergesort(left), mergesort(right))

# Merge függvény a MergeSort-hoz
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]: # ha a bal elem kisebb mint a jobb
            result.append(left[i]) # az eredményhez hozzáfűzzük a bal elem
            i += 1 # bal iteraciot noveljuk
        else:
            result.append(right[j])
            j += 1
    # mivel végigértünk az egyik részosztályon, de a másikon valószínűleg nem, hozzáadjuk a maradék elemeket
    result.extend(left[i:])
    result.extend(right[j:])
    return result # összefésült listát ad vissza

# Példa lista rendezésre
unsorted_list = [3, 6, 8, 10, 1, 2, 1]
    
# QuickSort használata
sorted_list_quick = quicksort(unsorted_list)
print("QuickSort eredmény:", sorted_list_quick)
    
# MergeSort használata
sorted_list_merge = mergesort(unsorted_list)
print("MergeSort eredmény:", sorted_list_merge)
