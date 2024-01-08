def minAmplitude(arr):
    if not arr:
        return -1
    elif len(arr) <= 4:
        return 0
    else:
        arr.sort() # O(nlogn)
        if arr[2] - arr[1] > arr[-2] - arr[-3]:
            if arr[3] - arr[2] > arr[-2] - arr[-3]:
                return arr[-1] - arr[3]
            else:
                return arr[-2] - arr[2]
        else:
            if arr[-2] - arr[-3] > arr[1] - arr[0]:
                return arr[-4] - arr[0]
            else:
                return arr[-3] - arr[1]
    
    
print(minAmplitude([-1, 3, -1, 8, 5,-1, 4]))