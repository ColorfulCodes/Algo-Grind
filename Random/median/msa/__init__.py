"""
There are 2 sorted arrays A and B of size n each.
Write an algorithm to find the median of the array
obtained after merging the above 2 arrays(i.e. array
of length 2n). The complexity should be O(log(n)).
"""

def median(c,b):
    c.extend(b)
    c = sorted(c)
    q = len(c)/2
    if len(c) % 2 ==0:
        me = (c[:q][-1] + c[q:][0])/2
        return me
    else:
        me = c[q:][0]
        return me
print median([1,12,30,4],[6,2,1,7])
print median([1,12,30,4],[6,200,9])
