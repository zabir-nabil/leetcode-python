# https://leetcode.com/problems/longest-palindrome/
# easy
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        
        cnt = Counter(s)
        
        is_odd = False
        
        ans = 0
        for k in cnt:
            ans += (cnt[k]//2)*2
            if cnt[k] % 2:
                is_odd = True
                
        if is_odd:
            ans += 1
            
        return ans
            