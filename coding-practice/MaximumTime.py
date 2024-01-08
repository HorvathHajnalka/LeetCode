def maxTime(s):
    arr = list(s)
    if arr[0] == "?":
        if arr[1] == "?" or arr[1] == "3" or arr[1] == "2" or arr[1] == "1" or arr[1] == "0" :
            arr[0] = "2"
        else:
            arr[0] = "1"
    if arr[1] == "?":
        if arr[0] == "2":
            arr[1] = "3"
        else:
            arr[1] = "9"
    if arr[3] == "?":
        arr[3] = "5"
    if arr[4] == "?":
        arr[4] = "9"
    return ''.join(arr)
        
print(maxTime("??:??"))