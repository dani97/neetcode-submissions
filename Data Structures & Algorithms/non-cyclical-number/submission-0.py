class Solution(object):
    def __init__(self):
        self.hset = set()

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n not in self.hset:
            self.hset.add(n)
            return self.isHappy(self.calc(n))
        else:
            return False
    def calc(self, n):
        sum = 0
        while n > 0:
            t = n%10
            sum += t**2
            n = n//10
        return sum
