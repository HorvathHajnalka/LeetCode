class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if len(fruits) == 0:
            return 0
        if len(fruits) == 1:
            return 1
        if len(fruits) == 2:
            return 2
        l = 0
        r = 1
        print(fruits)
        l_start = 0
        while fruits[r] == fruits[l] and  r < len(fruits) - 1:
            r += 1
        r_start = r
        maxfruits = r+1
        while r < len(fruits) - 1:
            while (fruits[r] == fruits[l] or fruits[r] == fruits[r_start]) and r < len(fruits) - 1:
                if fruits[r] == fruits[l]:
                    l_start = r
                while fruits[r] == fruits[l] and  r < len(fruits) - 1:
                    r += 1
                if r_start != r and fruits[r_start] == fruits[r]  and  r < len(fruits) - 1:
                    r_start = r
                while fruits[r] == fruits[r_start] and  r < len(fruits) - 1:
                    r += 1
            print(fruits[l:r])
            print(r)
            print(l)
            print(r_start)
            print(l_start)
            if r == len(fruits) - 1 and (fruits[r] == fruits[l] or fruits[r] == fruits[r_start]):
                curr_baskets = len(fruits[l:])
            else:
                curr_baskets = len(fruits[l:r])
            if curr_baskets > maxfruits:
                maxfruits = curr_baskets
            if fruits[r] != fruits[r_start] and fruits[r_start] != fruits[l_start]:
                l_start = r_start
            if fruits[r] != fruits[r_start]:
                r_start = r
            l = l_start
            #print(r)
        return maxfruits
        """
        i = 0
        j = 0
        maxfruits = 0
        curr_fruits = 0
        baskets = set()
        while i < len(fruits) and j < len(fruits):
            while i < len(fruits) and (len(baskets) < 1 or len(baskets) == 1 and fruits[i] in baskets):
                baskets.add(fruits[i])
                curr_fruits += 1
                i += 1
            j = i
            #minus = curr_fruits
            while j < len(fruits) and (len(baskets) < 2 or len(baskets) == 2 and fruits[j] in baskets):
                baskets.add(fruits[j])
                curr_fruits += 1
                j += 1
            print(curr_fruits)
            print(baskets)
            if curr_fruits > maxfruits:
                maxfruits = curr_fruits
            #baskets = set(fruits[i:j])
            baskets = set()
            #curr_fruits -= minus
            curr_fruits = 0
            
        return maxfruits"""
        