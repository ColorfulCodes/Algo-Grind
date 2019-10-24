# This algorithm moves 0s and Falses that translate to 0
def move_zeros(arr):
    read = 0
    write = 0
    
    if arr == []:
        return []

    if isinstance(arr,list) == False:
        raise ValueError("Invalid Argument. Please, use a list")

    for i in arr:
        if i is False or i !=0:
            arr[write] = arr[read]
            read += 1
            write += 1
        else:
            read += 1
    
    for i in range(len(arr)-1,-1,-1):
        if write == read:
            return arr
        else:
            write += 1
            arr[i]= 0
    return arr
            
move_zeros([False,1,0,1,2,0,1,3,"a"])