# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# idea: DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import Counter
    def dfs(self, r, path):
        #print(r.val)
        a1 = 0
        a2 = 0
        if r.left == None and r.right == None:
            path = path + str(r.val)
            #print(r)
            # check
            #print(path)
            #print('----')
            cnt = Counter(path)
            n_odd = 0
            
            for k in cnt:
                if cnt[k] % 2 == 1:
                    n_odd += 1
            
            if n_odd > 1:
                return 0
            return 1
            
        else:
            if r.left:
                a1 = self.dfs(r.left, path + str(r.val))
            if r.right:
                a2 = self.dfs(r.right, path + str(r.val))
            
            return a1 + a2

            
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans = self.dfs(root, '')
        #print('#####')
        return ans
        
        