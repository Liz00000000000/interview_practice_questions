#given an array of positive numbers and poistive number 'S', find the length of the 
#smallest contiguous subarray whose sum is greater than or equal to 'S'
#return zer if no such subarray exists 

# array = [2,1,5,2,3,2]
# S=7 #output is [5,2]

# array = [2,1,5,2,8]
# S=7 #output is [8]

# array = [3,4,1,1,6]
# S=8 # [3,4,1] or [1,1,6]
import math
array = [2, 1, 5, 2, 3, 2]
S = 7


def smallest_subarray(arr, S):
    windowStart, windowSum = 0, 0
    min_length = len(arr)+1
    
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= S:
            min_length = min(min_length, windowEnd-windowStart+1)
            windowSum -= arr[windowStart]
            windowStart += 1

    return min_length


print(smallest_subarray(array, S))



# def find_smallest_sub_array(array, S):
#     closest_sub_array = []
#     for num in range(len(array)):
#         new_arr = find_sub_array(array, num , S)
#         if new_arr:
#             closest_sub_array.append(new_arr)

#     return len(smallest_sub_array(closest_sub_array))


# def find_sub_array(array, num , S):
#     if array[num] >= S:
#         return [array[num]]
#     elif len(array) <= num +1 or len(array) <= num + 2:
#         return None
#     elif array[num] + array[num+1] >= S:
#         return [array[num], array[num+1]]
#     elif array[num] + array[num+1] + array[num+2] >= S:
#         return [array[num], array[num+1], array[num+2]]
#     else:
#         return None

# def smallest_sub_array(array):
#     return_array = array[0]
#     for sub_array in array:
#         if len(sub_array) < len(return_array):
#             return_array = sub_array
#     return return_array



# print(find_smallest_sub_array(array,S))