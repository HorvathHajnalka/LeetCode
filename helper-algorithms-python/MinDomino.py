# My Solution
def minDominoRotations(tops, bottoms):
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
print('end', minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))

# Short Solution

def minDominoRotations(tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        def check(x) :
            rotation_a, rotation_b = 0, 0

            for i in range(len(tops)) : # végigiterálunk a 2 tömbön
                if tops[i] != x and bottoms[i] != x : #ha egyik sem egyezik a keresett értékkel kilépünk
                    return -1
                # ha valamelyik érték megegyezik, akkor növeljük az ellenkező oldal számlálóját
                elif tops[i] != x :
                    rotation_a += 1
                elif bottoms[i] != x :
                    rotation_b += 1
            # ha nem lépett ki a ciklusból még akkor a minimumcserét adjuk vissza
            return min(rotation_a, rotation_b)
        
        first = check(tops[0])
        # ha megtaláltuk vagy
        if first != -1 or tops[0] == bottoms[0] :
            return first
        #
        return check(bottoms[0])
print('end', minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))