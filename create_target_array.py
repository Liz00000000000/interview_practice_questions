#Given two arrays of integers nums and index. 
#Your task is to create target array under the 
#following rules:
#Initially target array is empty.
#From left to right read nums[i] and index[i], 
#insert at index index[i] the value nums[i] in target array.
#Repeat the previous step until there are no elements to read 
#in nums and index. Return the target array.
#It is guaranteed that the insertion operations will be valid.

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
#Output: [0,4,1,3,2]

def create_target(nums,index):
    return_arr = []
    for i in range(len(nums)):
        print(return_arr)
        new_index = index[i]
        if new_index < len(return_arr):
            new_end_array = return_arr[new_index:]
            new_num = nums[i]
            return_arr[new_index] = new_num
            return_arr = return_arr[:new_index+1]
            return_arr += new_end_array
        else:
            return_arr.append(nums[i])
    
    return return_arr


print(create_target(nums,index))