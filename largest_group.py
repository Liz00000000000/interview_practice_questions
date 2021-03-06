#Given an integer n. Each number from 1 to n is grouped according to the sum of 
#its digits. 
#Return how many groups have the largest size.
n = 13
#Output: 4
#Explanation: There are 9 groups in total, they are grouped according sum 
#of its digits of numbers from 1 to 13:
#[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups 
#with largest size.
#n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
#n = 15
#Output: 6
#n = 24
#Output: 5

def largest_group(n):
    nums = []
    for i in range(1,n):
        j = i/n
        nums.append([j])

    return nums


print(largest_group(n))