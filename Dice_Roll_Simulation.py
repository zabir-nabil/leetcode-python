# https://leetcode.com/problems/dice-roll-simulation/
# simple dp

class Solution:
    def rec(self, i, prev, prev_cnt):
        if prev_cnt > self.rollMax[prev]:
            return 0
        if i > self.n: # reached a solution
            return 1
        if self.dp[i][prev][prev_cnt] !=-1:
            return self.dp[i][prev][prev_cnt]
        
        # solution
        m = 1000000000+7
        
        ans = 0
        for k in range(1,7):
            if k == prev:
                ans = (ans + self.rec(i+1, k, prev_cnt + 1))%m
            else:
                ans = (ans + self.rec(i+1, k, 1))%m
        
        self.dp[i][prev][prev_cnt] = ans
        return self.dp[i][prev][prev_cnt]
    
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.dp = [[[-1 for _ in range(16)] for _ in range(7)] for _ in range(5002)]
        self.n = n
        self.rollMax = [99999999] + rollMax
        m = 1000000000+7
        ans = self.rec(1, 0, 0) % m
        
        return ans
        