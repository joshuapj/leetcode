"""
input:  s = char []
        t = char []

output: str: char []

find the largerst common substring between the two string inputs and return it

Cases:
1) s and t are of the same length and contain the same chars
2) s and t have no common substring


Pseudo
for i in range of the smaller string, start with that length and decrement
    if len of strings are not divisible by i:
        continue
    else:
        get how many times strings are divisible by i
        if the str1[:i] * factor == str2[:i]* factor:
            return the str1[:i]
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:    
        for i in range(min(len(str1), len(str2)), 0, -1):
            if len(str1) % i != 0 or len(str2) % i != 0:
                continue
            else:
                factor1 = len(str1) // i
                factor2 = len(str2) // i
                if str1[:i]*factor1 == str1 and str1[:i]*factor2 == str2:
                    return str1[:i]
        return ""