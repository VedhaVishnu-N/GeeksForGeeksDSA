#Import necessary libraries
from array import array
import time

#define insertion sort function
def Selection_sort(arr):
    n=len(arr)
    for i in range(1,n):
        insert_index=i
        current_value= arr.pop(i)
        for j in range(i-1,-1,-1):
            if arr[j]>current_value:
                insert_index=j
        arr.insert(insert_index,current_value)
        


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