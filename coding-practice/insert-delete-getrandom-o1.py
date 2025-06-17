import random
class RandomizedSet(object):

    def __init__(self):
        self.random_set = set()
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        success = val not in self.random_set
        self.random_set.add(val)
        return success

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        success = val in self.random_set
        self.random_set.discard(val)
        return success
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.sample(self.random_set, 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()