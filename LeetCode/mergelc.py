Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]



# Where I was going originally.
# Incorrect code below

def merge(num1,m,num2,n):
  i = 0
  j = 0
  while i <=len(nums2):
    if nums2[i] <= nums1[j]:
      temp = nums1[j]
      nums1[j] = nums2[i]
      j += 1
    else:

# nums1 = [2,5,6]
# nums2 = [1,3,5]
# I don't know what i'm doing. Time to look at solutions.
--------------

#Other Smart people's code.

ex 1

def merge(nums1, m, nums2, n):

    nums1.reverse()
    for i in range(len(nums2)):
        nums1[i] = nums2[i]
    nums1.sort()

merge([1,2,3,0,0,0], 3, [2,5,6], 3)

------------------------------------

ex 2

def merge(nums1, m, nums2, n):

    i = m + n - 1
    m -= 1
    n -= 1

    while m > -1 and n > -1:
        if nums1[m] > nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1

        i -= 1

    # If necessary, add rest of nums2 to the front of the list
    if m == -1:
        nums1[:i+1] = nums2[:n+1]

merge([1,2,3,0,0,0], 3, [2,5,6], 3)

------------------------------------------------------

# This code is crazy Haha

def merge(nums1, m, nums2, n):

    nums1[m:] = nums2
    nums1.sort()

merge([1,2,3,0,0,0], 3, [2,5,6], 3)

ex 4: I do not know why this works and j keeps iterating even after m

def merge(nums1, m, nums2, n):

    j = 0
    for i in range(n):
        while j <m and nums2[i]>=nums1[j]:
            j += 1
        nums1.insert(j,nums2[i])
        m += 1
        nums1.pop()

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
