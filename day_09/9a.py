
'''
for  each line: take the line as an array
create a new array with the differences of the above array and store the last value of the array
check if all elements of the array are zero
if so return upwartds
'''
import numpy as np

# takes in np array and returns an array of its differences
def reduce_array(arr):

  #create zero array
  l = len(arr)
  zeros = np.zeros(l)

  

  #compare array to zeroes
  is_zeros = (arr == zeros).all()
  print(is_zeros)

  #if not repeat again
  if not is_zeros:
    arr = np.absolute(arr[1:] - arr[:l-1])
    print(arr)
    arr = reduce_array(arr)

  print('returning', arr)
  return arr  





print(reduce_array(np.array([1, 3, 6, 10, 15, 21])))

