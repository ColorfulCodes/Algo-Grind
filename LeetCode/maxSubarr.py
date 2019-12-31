# Given an integer array nums, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, 
# try coding another solution using the divide and 
# conquer approach, which is more subtle.

# Done with Kidane's Algorithm
#If i can benefit from it's predecessor, add it to i,
# if not, move along as current i would be the maximum
def maxSub(a):
    for i in range(1, len(a)):
        if a[i-1]> 0:
            a[i] += a[i-1]
    return max(a)
            
            
maxSub([-2,1,-3,4,-1,2,1,-5,4])

            