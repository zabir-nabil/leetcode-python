# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3308/
# solution idea: bitwise and pattern

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mo = m # making copy
        no = n # making copy
        p = 0 # power count
        
        ans = 0
        while(m>0 and n>0):
            mb = m%2 # binary
            nb = n%2 
            
            if ((no-mo) < 2**(p)) and (mb == nb):
                ans += 2**(p)*(mb) # this is a tricky one to multiply for 0 cases
                
            p += 1
            m//=2
            n//=2
            
        return ans