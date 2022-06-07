maximum sum rotation
import sys
#also can use math module
 
# Returns maximum value of i * arr[i]
def maxSum(arr, n):
 
    # Initialize result
    res = -sys.maxsize
 #use to return the max num in feom a list
#and storie it in bitwise form
#the -sign converts it to a interger
 
    # Consider rotation beginning with i
    # for all possible values of i.
    for i in range(0, n):
 
 
        # Initialize sum of current rotation
        curr_sum = 0
     
        # Compute sum of all values. We don't
        # actually rotation the array, but
        # compute sum by finding indexes when
        # arr[i] is first element
        for j in range(0, n):
         
            index = int((i + j)% n)
            curr_sum += j * arr[index]
     
 
        # Update result if required
        res = max(res, curr_sum)
    return res
 
# Driver code
arr = [8, 3, 1, 2]
n = len(arr)
 
print(maxSum(arr, n))
