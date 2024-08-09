#Import necessary libraries
from array import array
import time

#define selection sort function
def Selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

#create an array
arr= array('i',[442,64,3,6,7,2])

#note start time
start_time=time.time()

#call the function
Selection_sort(arr)

#calculate end time
end_time=time.time()

#print the output
print(start_time,end_time)
print("executrion time is ",end_time-start_time)

print(arr)