class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        distance = 0
        height1 = 0
        height2 = 0
        i = 0
        maxarea = 0
        while i < len(height):
            j = i+1
            while j < len(height):
                area = (j-i)*min(height[i], height[j])
                if area > maxarea:
                    maxarea = area
                j += 1
            i += 1
        return maxarea
        """
        distance = len(height)-1
        height1 = 0
        height2 = len(height)-1
        maxarea = 0
        while height1 != height2:
            area = (height2-height1)*min(height[height1], height[height2])
            if area > maxarea:
                maxarea = area
            if height[height1] > height[height2]:
                height2 -= 1
            else:
                height1 += 1
        return maxarea
        