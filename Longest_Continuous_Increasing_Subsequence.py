# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# easy, trikcy part: missing any start solution will have c_ans = 1 not 0

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        
        c_ans = 0 # current max
        
        prev_li = - 99999999 # - inf
        for li in nums:
            if li > prev_li:
                c_ans += 1
                ans = max(ans, c_ans)
            else:
                c_ans = 1 # a single element solution, this can't be 0
                
            prev_li = li
        
        return ans