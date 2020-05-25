# https://leetcode.com/problems/max-dot-product-of-two-subsequences/
# solution idea: dp + state propagation

class Solution:
    
    def dp(self, i, j, b):
        #print(self.numsg1)
        #print(len(self.memo)), i
        #print(len(self.memo[0])), j
        if i >= len(self.nums1):
            if b == 0:
                return -99999999
            return 0
        if j >= len(self.nums2):
            if b == 0:
                return -99999999
            return 0
        if self.memo[i][j][b] != -9999999:
            return self.memo[i][j][b]
        
        op1 = (self.nums1[i] * self.nums2[j]) + self.dp(i+1,j+1, 1)
        op2 =  self.dp(i+1,j, b)
        op3 =  self.dp(i,j+1, b)
        op4 = self.dp(i+1, j+1, b)
        
        self.memo[i][j][b] = max(op1, op2, op3, op4)
        return self.memo[i][j][b]
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1 = nums1
        self.nums2 = nums2
        
        self.memo = [[[-9999999 for k in range(2)] for i in range(len(nums2))] for j in range(len(nums1))]
        ans = self.dp(0,0,0)
        
        return ans
        
        