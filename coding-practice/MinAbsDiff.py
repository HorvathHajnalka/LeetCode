"""def minAbsDiff(arr):
    goal = sum(arr) //2
    minw = min(arr)
    weights = []
    for i in range(goal+1): 
        if i > minw:
            weights.append([float('inf')])    
        elif i == minw:
            weights.append([1])
        else:
            weights.append([0])
    
    for i in range(1, goal+1): #O(n^2)
        down = 1
        up = i-1
        end = i//2
        if i in arr:
            weights[i][0] = 1
            weights[i].append(i)
        else:
            while up > end:
                curr = weights[up][0] + weights[down][0]
                if curr < weights[i][0]:
                    weights[i].clear()
                    weights[i].append(curr)
                    upidx = 1
                    while upidx < len(weights[up]):
                        weights[i].append(weights[up][upidx])
                        upidx += 1
                    downidx = 1
                    while downidx < len(weights[down]):
                        weights[i].append(weights[down][downidx])
                        downidx += 1
                up -= 1
                down += 1
            if up == down:
                curr = weights[up][0] + weights[down][0]
                if curr < weights[i][0]:
                    weights[i].clear()
                    weights[i].append(curr)
                    upidx = 1
                    while upidx < len(weights[up]):
                        weights[i].append(weights[up][upidx])
                        upidx += 1
                    downidx = 1
                    while downidx < len(weights[down]):
                        weights[i].append(weights[down][downidx])
                        downidx += 1
    print(weights)
    sum1 = 0
    for i in range(1, len(weights[-1])):
        sum1 += weights[-1][i]
    return (sum(arr) - sum1) - sum1
        
print(minAbsDiff([10,5,6]))"""

def minAbs(nums):
  middle =sum(nums)//2
  n=len(nums)
  dp=[[0 for _ in range(middle+1)] for x in range(n+1)] # n+1 darab middle hosszú lista
  #dp  egy kétdimenziós tömb, ahol a sorok a feldolgozott folyamatokat (processes) képviselik, a oszlopok pedig a lehetséges terhelésértékeket (loads).
  for i in range(1,n+1):
      print(dp)
      for j in range(1,middle+1):
          if nums[i-1]<=j: # az aktuális folyamat terhelése (nums[i-1]) kisebb vagy egyenlő-e a jelenlegi terhelésértékkel (j)
              dp[i][j]=max(dp[i-1][j], nums[i-1]+dp[i-1][j-nums[i-1]])
              # dp[i][j] értéke a maximumot veszi fel a következő két érték közül:
              # Az előző sorban (dp[i-1][j]), amikor nem vesszük fel az aktuális folyamatot a szerver terhelésébe.
              # Az aktuális folyamat terhelése hozzáadva az előző sorban (dp[i-1][j-nums[i-1]]) számolt terheléshez.
          else:
              dp[i][j]=dp[i-1][j] # átmásoljuk az előző sor értékét az aktuális sorba
  '''return second server loads - first server loads'''
  print(dp)
  return (sum(nums)-dp[-1][-1])-dp[-1][-1] 
'''four testcases'''
#print(minAbs([1, 2, 3, 4, 5]))
print(minAbs([10,2,9,2]))
#print(minAbs([]))
#print(minAbs([1]))