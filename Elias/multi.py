array1 = [1,2,2]
array2 = [1,2,2]

def multiply_arrays(array1, array2):
    
    output_len = len(array1) + len(array2)
    output_array = [0 for i in range(output_len)]

    #output array, 2 input arrays
    # a double for loop, that iterates through both input arrays
    for i in reversed(range(len(array1))):
        for j in reversed(range(len(array2))):
            new_number = array1[i] * array2[j]
            new_index = i + j + 1
            output_array[new_index] += new_number
            output_array[new_index - 1] = new_number // 10
            output_array[new_index] = output_array[new_number] % 10


    return output_array


print(multiply_arrays(array1, array2))
    #  [7]
    #x [7]
    #[ 0, 0]
    #[1, 2]
    #[1, 2]
    #-------
    # 24
    #120
    #144
    # output_array_length = len(array1) + len(array2)
    # im saying we should have an output array because we do know before multiplying 7*7 its 49 which is 2 array slots
    # maybe this isnt universal like with 0 * 0, but look
    #
    # lets say we return an array of the length of the sum of both lengths of the input arrays
    #
    # len 7 = 1, 1 + 1 = 2 => [4,9]
    # len 0 = 1, 1+1 = 2 => [0,0] => this is also 0
    #
    # 10 * 1,000 = len(2) + len(4) = len(6)
    # 10000 == len(5)
    #
    # We can change the length of the array, to fit the product afterwards.
    # [0, 1, 0,0,0 ,0]
    # 0   1  2 3 4 5  == len(6)
    # We can just remove the 0 at the front from the array and we have our answer
#  0  =>  [0]
#x 0  =>* [0]
#  0  =>  [0]
#  7  =>  [7]
#x 7  =>x [7]
# 49  =>  [4, 9]