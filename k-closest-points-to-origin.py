class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        mindistances = [float('inf') for i in range(0, k)]
        minpoints = [[] for i in range(0, k)]
        for point in points:
            # curr_distance = (point[0]**2 + point[1]**2)**0.5
            curr_distance = point[0]**2 + point[1]**2
            #maxd = max(mindistances)
            maxidx = mindistances.index(max(mindistances))
            if curr_distance < mindistances[maxidx]:
                mindistances[maxidx] = curr_distance
                minpoints[maxidx] = point
        return minpoints