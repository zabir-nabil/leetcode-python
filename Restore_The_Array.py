# https://leetcode.com/problems/restore-the-array/
# iterative DP, can be done in O(1) memory

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        m = 1000000000+7
        
        dp = [0]*(len(s)+5)
        
        
        for i in range(len(s)):
            for j in range( max(0, i-10), i+1 ):
                c_num = int(s[j:i+1])
                if c_num <= k and c_num !=0 and s[j]!='0':
                    if j==0:
                        dp[i] = (dp[i] + 1)%m # base case
                    else:
                        dp[i] = (dp[i] + dp[j-1])%m
                        
        # print(dp)
        
        
        return dp[len(s)-1]
                    
            
                    
        