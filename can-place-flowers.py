class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
       # if sum(flowerbed)+n <= len(flowerbed) // 2 :
        #    return True
        if n == 0:
            return True
        if(len(flowerbed) == 1):
            if flowerbed[0] == 0 and n == 1:
                return True
            return False
        cflowerbed = flowerbed
        unused = n
        i = 0
        if cflowerbed[0] == 0 and cflowerbed[1] == 0 and unused != 0:
            cflowerbed[0] =1
            unused -= 1
            i += 1
        while i < len(cflowerbed)-2 and unused != 0:
            if cflowerbed[i] == 0 and cflowerbed[i+1] == 0 and cflowerbed[i+2] == 0:
                cflowerbed[i+1] = 1
                unused -= 1
                i += 1
            i += 1
        if len(cflowerbed) != 2 and cflowerbed[-2] == 0 and cflowerbed[-1] == 0 and unused != 0:
            unused -=1
            cflowerbed[-1] = 1
        if unused == 0:
            return True
        return False
        