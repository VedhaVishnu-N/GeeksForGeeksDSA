from array import array
import time

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]

    sortedleft=merge_sort(left_arr)
    sortedright=merge_sort(right_arr)

    return(merge(sortedleft,sortedright))

def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

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

print(merge_sort(arr))        