def mostBooked(arr):
    books = {}
    maxbook = 1
    maxrooms = arr
    for elem in arr:
        if elem[0] == "+":
            room = elem[1:]
            if room not in books:
                books[room] = 1
            else:
                books[room] += 1
                if books[room] > maxbook:
                    maxrooms = [room]
                elif books[room] == maxbook:
                    maxrooms.append(room)
    return min(maxrooms)

print(mostBooked(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]))