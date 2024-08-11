class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        topcounts = [0 for i in range(0,7)]
        downcounts = [0 for i in range(0,7)]
        #print(topcounts, downcounts)
        for i in range(0, len(tops)): #O(n)
            topcounts[tops[i]] += 1
            downcounts[bottoms[i]] += 1
        minrotations = float('inf')
        #print(topcounts, downcounts)
        while max(topcounts) != 0: #O(1)
            #print('top')
            maxi = 0
            maxidx = 0
            for j in range(0, len(topcounts)): #O(1)
                if topcounts[j] > maxi:
                    maxi = topcounts[j]
                    maxidx = j
                #print('max')
            curr = maxidx
            i = 0
            ok = True
            curr_rot = 0
            #print(tops, bottoms)
            while i < len(tops) and ok:
                # print('i',i)
                #print(tops[i], bottoms[i], curr)
                if tops[i] != curr and bottoms[i] != curr:
                    ok = False
                elif  tops[i] != curr and bottoms[i] == curr:
                    curr_rot += 1
                i+= 1
            #print('ok', ok)
            #print(minrotations, 'min')
            if ok and curr_rot < minrotations:
                minrotations = curr_rot
            topcounts[maxidx] = 0
        #print(minrotations, 'min')
        while max(downcounts) != 0: #O(1)
            #print("down")
            
            maxi = 0
            maxidx = 0
            for j in range(0, len(downcounts)): #O(1)
                if downcounts[j] > maxi:
                    maxi = downcounts[j]
                    maxidx = j
            curr = maxidx
            #print(curr, 'curr')
            #print(downcounts, 'downcounts')
            i = 0
            ok = True
            curr_rot = 0
            #print(bottoms, 'bottoms')
            while i < len(bottoms) and ok:
                if bottoms[i] != curr and tops[i] != curr:
                    ok = False
                elif bottoms[i] != curr and tops[i] == curr:
                    curr_rot += 1
                i+= 1
            #print(ok, 'ok')
            #print(curr_rot, 'curr_rot')
            if ok and curr_rot < minrotations:
                minrotations = curr_rot
            downcounts[maxidx] = 0
        if minrotations == float('inf'):
            return -1
        else:
            return minrotations