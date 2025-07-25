
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt = 0
        res = ''

        while pt < min(len(word1), len(word2)):
            res += word1[pt]
            res += word2[pt]
            pt += 1
        
        if len(word1) > len(word2):
            res += word1[pt:]
        
        if len(word2) > len(word1):
            res += word2[pt:]
        
        return res
        
