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


def minWindow(s, t):
    count = 0
    start = 0
    hold = {}
    smallest = s
    exists = False

    
    for letter in t:
        if letter not in hold:
            hold[letter] = 1
            count +=1
        else:
            hold[letter] += 1
    
    
    for end in range(len(s)):
        if s[end] not in hold:
            continue
        hold[s[end]] -= 1
        if hold[s[end]] == 0:
            count -= 1
            
        while count == 0:
            exists = True
            if len(s[start:end+1]) < len(smallest):
                smallest = s[start:end+1]
            goLeft = s[start]
            start += 1
            if goLeft not in hold:
                continue
            hold[goLeft] += 1
            if hold[goLeft] == 1:
                count += 1
                break
    
    if exists == False:
        return ""
    return smallest
    

    
minWindow("ADOBECODEBANC", "ABC")



