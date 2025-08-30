"""
input:  s = char []
        t = char []

output: bool ret

check if s contains contains some of the characters in t in the order that they appear in t.

Edge Cases:
1) a new string can be formed, given that bith s and t have characters
2) s is of length 0
3) t is of length 0

Two pointer - keep two indexes for the array that your working on.

s = abc
t = ahbgdc

Pseudo
i = 0 // for keeping track of s
j = 0 // for keeping track of t

for j in range(length of t):
    if t[j] is equal to s[i]:
        i += 1
        
    else if t[j] is not equal to s[i]:
        continue

if i is equal to the length of s, then return True
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
                if i >= len(s):
                    return True
            elif t[j] != s[i]:
                continue

        return i == len(s)


        