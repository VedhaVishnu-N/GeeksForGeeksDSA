#import necessary modules(time and array)
import time
from array import array

#define binary_search function
def Binary_search(arr,n):
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


#create an array
arr=array('i',[44,2,5,63,7,8,12])

#start time
start_time =time.perf_counter()

#call binary_search function
Binary_search(arr,len(arr))

#end time
end_time=time.perf_counter()

#calculate_time
execution_time = end_time - start_time

#print the output values
print("execution time:",execution_time)
print(arr)