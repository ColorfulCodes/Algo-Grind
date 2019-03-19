# # only one or two steps at a time
# Climbing Stairs: Time - O(n), space: O(n)
#  by ramineedi
# You can put it in a function or not.
# we are adding 2 previous amounts to next
# if it's 3 steps helper(n-1) + n-2 + n-3
#Bottom up
def climbStairs(n):
    #This is like memoization. We are storing results in dictionary and not
    #recalculating each time
    store = {} # save the data to avoid recalculations
    def helper(n):
        #if n ==0 return 1 or n < 0 return 0
  # if we are at 3, we already know how many steps to get to 1 and 2
        #Our base cases
        if n == 1 or n == 2:
            return n
        elif n in store:
            return store[n]
        else:
            store[n] = helper(n - 1) + helper(n - 2)
            return store[n]

    return helper(n)

climbStairs(4)
