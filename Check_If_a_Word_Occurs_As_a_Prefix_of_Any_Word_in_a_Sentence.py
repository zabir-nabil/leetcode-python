# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# idea: easy, string

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sen = sentence.split(' ')
        
        for i, w in enumerate(sen):
            if w.startswith(searchWord):
                return i+1
            
        return -1
        