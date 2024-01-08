class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        again = True
        againindex = 0
        while again:
            findagain = False
            i = againindex
            triple = [nums[againindex]]
            first = nums[againindex]
            second = nums[againindex]
            third =nums[againindex]
            while len(triple) != 3 and i != len(nums):
                if len(triple) == 1:
                    if nums[i] < first:
                        first = nums[i]
                        triple[0] = first
                    if nums[i] > first:
                        second = nums[i]
                        triple.append(second)
                if len(triple) == 2:
                    if nums[i] > second:
                        third = nums[i]
                        triple.append(third)
                        return True
                    if nums[i] < second and nums[i] > first:
                        second = nums[i]
                        triple[1] = second
                    if nums[i] < first and not findagain:
                        againindex = i
                        findagain = True
                i += 1
            if i == len(nums) and not findagain:
                print(triple)
                return False
