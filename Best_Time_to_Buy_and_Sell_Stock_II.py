# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

# Note: DP solution gets TLE

class Solution:
    import sys
    sys.setrecursionlimit(60000)
    def rec(self, i):
        if i >= len(self.memo):
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        
        # I'm buying on ith day
        c1 = self.prices[i]
        c2 = 0
        for j in range(i+1,len(self.prices)):
            # lets say I'm seliing on jth day
            c2 = max(c2, (self.prices[j]-c1) + self.rec(j+1))
            
        # I'm not buying on ith day
        
        c2 = max(c2, self.rec(i+1)) # just go to next day
        
        self.memo[i] = c2
            
        return c2
        
    def maxProfit(self, prices):
        self.prices = prices
        self.memo = [-1]*len(prices)
        
        ans = self.rec(0)
        
        return ans


# solution time test
import numpy as np
import time

s = Solution()

a = np.random.randint(low = 0, high = 3, size = 5000)
t1 = time.time()
ans = s.maxProfit(a)
t2 = time.time()
print(ans)
print(t2-t1)