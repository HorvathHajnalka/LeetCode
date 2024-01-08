def minChairs(s, e):
    maxtime = max(e) # O(n)
    headcount = [0 for _ in range(maxtime+1)]
    for i in range(0, len(s)): # O(n)*max
        for j in range(s[i], e[i]):
            headcount[j]+= 1
    return max(headcount)
        
print(minChairs([1, 2, 6, 5, 3], [5, 5, 7, 6, 8]))