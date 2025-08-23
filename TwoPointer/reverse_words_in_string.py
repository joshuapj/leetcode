"""
This contains 3 solutions:
1) My solution (not optimal in the slightest)
2) A solution using python built-ins
3) A two pointer solution
"""
import collections

# SOLUTION 1
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        current_string = ""

        for i in range(len(s)):
            # check if it is a new word
            if current_string == "":
                # if it is empty, check if the current index is a space
                if s[i] != " ":
                    current_string += s[i]
            # if word is being checked, and this is a space, store current word
            elif s[i] == " ":
                # insert the word at the head to reverse it
                if res == "":
                    res = current_string
                else:
                    res = current_string + " " + res
                # reset the current string
                current_string = ""
            # if the current index is a char, then append it to the current string
            else:
                current_string += s[i]
        if current_string != "":
            if res == "":
                res = current_string
            else:
                res = current_string + " " + res
        return res

# SOLUTION 2 
class Solution:
    def reverseWords(self, s: str) -> str:
        # remove all of the white space and store the words in a list
        remove_ws = s.split()
        # reverse the order of the list
        reverse_order = remove_ws[::-1]
        # join the reversed list with a space
        join_reversed = " ".join(reverse_order)
        
        return join_reversed


class Solution:
    def reverseWords(self, s: str) -> str:
        # string builder
        # this makes a double ended queue. Allows us to append to left and right end
        str_builder = collections.deque()
        i = 0
        start = -1

        while i < len(s):
            if s[i] != " ":
                # keep track of the location of first character in a word
                start = i
                # while index valid and value is not a ws, keep going
                while i < len(s) and s[i] != " ":
                    i += 1
                # at whitespace/end it breaks, append to the left end (start of the queue) the substring from start to i
                str_builder.appendleft(s[start:i])
                # decrement i so we dont skip any iterations
                i -= 1
            i += 1
        return " ".join(str_builder)