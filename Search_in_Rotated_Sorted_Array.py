# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/530/week-3/3304/

# solution idea: 2 binary searches, one for finding pivot, another for finding element
# things to note: for any binary search, keep a linear search for small (n<5) arrays
# to avoid edge cases

class Solution:
    def bin_search1(self, i, j): # for finding pivot
        # binary search 1 for finding the pivot
        if self.nums[i] < self.nums[j]:  # <= will give WA
            return 0 # no rotation
        l = i
        r = j
        m = 0
        while l<r:
            if r == l+1:
                return r # the index from which second segment starts
            m = (l+r)//2
            if self.nums[l] <= self.nums[m]:
                l = m
            else:
                r = m
        return m
    
    def bin_search2(self, i, j, k): # for finding the key
        # binary search 2 for finding the key
        
        if (j-i) <= 4:
            if k in self.nums[i:j+1]:
                return self.nums[i:j+1].index(k) + i
            else:
                return -1

        l = i
        r = j
        m = 0
        while l<r:
            if r == l+1:
                if self.nums[l] == k:
                    return l
                elif self.nums[r] == k:
                    return r
                else:
                    return -1
                
            m = (l+r)//2
            if self.nums[m] <= k:
                l = m
            else:
                r = m
        return -1
                
            
        
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        
        if len(nums) == 0:
            return -1
        
        if len(nums) <= 5:
            if target in nums:
                return nums.index(target)
            else:
                return -1
        

        pivot = self.bin_search1(0, len(nums)-1)
        # print(pivot)
        
        if pivot == 0: # no rotation
            ans = self.bin_search2(0, len(nums)-1, target)
        else:
            ans = self.bin_search2(0, pivot-1, target)
            ans = max(ans, self.bin_search2(pivot, len(nums) - 1, target))

            
        return ans
        
        