# https://leetcode.com/problems/max-consecutive-ones/
# easy

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ans = 0
        
        cur_ans = 0

        for a_i in nums:
            if a_i == 1:
                cur_ans += 1
                max_ans = max(max_ans, cur_ans)
            else:
                cur_ans = 0
                
        return max_ans
        