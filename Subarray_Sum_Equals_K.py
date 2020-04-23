# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3307/

# solution idea: keep a hashmap, while iterating over cum sum check if in the previous cum sums there exists
# any current cum_sum - k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0:1} # we need to keep count, initially there is one zero
        
        cum_sum = 0
        ans = 0
        for i in nums:
            cum_sum += i
            if (cum_sum-k) in hash_map: # d in dict O(1)
                ans += hash_map[cum_sum-k]
            
            if cum_sum in hash_map:
                hash_map[cum_sum] += 1
            else:
                hash_map[cum_sum] = 1
                
        return ans
            