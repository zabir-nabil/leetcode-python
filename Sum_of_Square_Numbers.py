# https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        # lower search bound => 2x^2 = c, x = sqrt(c/2), but if a = 0, x = sqrt(c)
        import math
        
        for a in range( int(math.sqrt(c)) + 2 ):
            b2 = c - (a**2)
            if b2 < 0:
                continue
            b = int(math.sqrt(b2))
            if b*b == b2:
                return True
            
        return False
        