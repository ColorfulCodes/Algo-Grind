# Given a string S and a string T, find the minimum window in S which will contain
# all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

def minWindow(s,t):
    smallest = ""
    # check if each iteration has each character


    for i in s:
        for j in range(1, len(s))
            while i < len(t):
                i+= 1
