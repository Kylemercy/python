def rotate(arr, n):
    x = arr[n - 1]
     
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];
         
    arr[0] = x;
 
 
# Driver function
arr= [1, 2, 3, 4, 5]
n = len(arr)

rotate(arr, n)
 
print ("\nRotated array is")
for i in range(0, n):
    print (arr[i],end = " ")
    
    
#rotating an array in a clockwise direction 