# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# idea: deque, window

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        from collections import deque
        max_ans = 0
        
        
        d = deque()
        
        cur_ans = 0
        for i, c in enumerate(s):
            if len(d) == k:
                dl = d.popleft()
                if dl in 'aeiou':
                    cur_ans -= 1
                d.append(c)
                if c in 'aeiou':
                    cur_ans += 1
            else:
                d.append(c)
                if c in 'aeiou':
                    cur_ans += 1
                    
            max_ans = max(cur_ans, max_ans)
            
        return max_ans