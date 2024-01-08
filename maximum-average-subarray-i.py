class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        i = 0
        j = k
        maxsum = sum(nums[i:j])
        while j < len(nums)+1:
            curr = sum(nums[i:j])
            if curr > maxsum:
                maxsum = curr
            i+= 1
            j+= 1
        return float(maxsum)/float(k)
    
        i = 0
        j = k-1
        #maxi = 0
        maxsum = sum(nums[i:j+1])
        while j < len(nums):
            if nums[j] > nums[i-1]:
                curr = sum(nums[i:j+1])
                if curr > maxsum:
                    #maxi = i
                    maxsum = curr
            i+= 1
            j+= 1
            #print(maxi)
        maxsum = float(maxsum)
        #print(maxi)
        return maxsum/float(k)

        i = 0
        j = k-1
        maxi = 0
        while j < len(nums):
            if nums[j] > nums[i-1]:
                maxi = i
            i+= 1
            j+= 1
            print(maxi)
        #print(maxi)
        maxsum = sum(nums[maxi:maxi+k])
        return maxsum/float(k)"""
        sum_arr=sum(nums[:k])    
        avg=float(sum_arr)/float(k)
        for i in range(1,len(nums)-k+1):
            sum_arr=sum_arr-nums[i-1]
            sum_arr=sum_arr+nums[i+k-1]
            avg=max(avg,float(sum_arr)/float(k))
        return avg
        