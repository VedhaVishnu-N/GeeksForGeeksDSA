#import necessary libraries
from array import array
import time

#defining quick sort
def quick_sort(arr):
    length=len(arr)
    if length<=1:
        return arr
    else:
        pivot=arr.pop()
    item_higher=[]
    item_lower=[]
    for item in arr:
        if item<pivot:
            item_lower.append(item)
        else:
            item_higher.append(item)
    return quick_sort(item_lower) + [pivot] +quick_sort(item_higher)
    
#create an array
arr= array('i',[442,64,3,6,7,2])

#note start time
start_time=time.time()

#call the function


#calculate end time
end_time=time.time()

#print the output
print(start_time,end_time)
print("executrion time is ",end_time-start_time)

print(quick_sort(arr))