# https://leetcode.com/problems/license-key-formatting/

# easy, but tricky logic cases if i < len(S) - 1: will fail
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "")[::-1]
        
        O_S = ""
        num_block = 0
        for i, s in enumerate(S):
            if num_block == K:
                if i <= len(S) - 1:
                    O_S = O_S + "-"
                num_block = 0
            num_block += 1
            O_S = O_S + s.upper()
            
        return O_S[::-1]
                