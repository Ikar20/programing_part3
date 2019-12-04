#def mergeSort(array): 
  #  sorted_array = array

 #   if len(array) >1: 
  #      mid = len(array) // 2  
   #     left = array[:mid] 
    #    right = array[mid:] 
  
   #     mergeSort(left)
   #     mergeSort(right) 
  
    #    left_index = right_index = k = 0
          
   #     while left_index < len(left) and right_index < len(right): 
   #         if left[left_index].price < right[right_index].price: 
     #           array[k] = left[left_index] 
     #           left_index += 1
    #        else: 
  #              array[k] = right[right_index] 
  #              right_index += 1
  #          k += 1
          
   #     while left_index < len(left): 
   #         array[k] = left[left_index] 
   #         left_index += 1
  #          k += 1
          
  #      while right_index < len(right): 
  #          array[k] = right[right_index] 
 #           right_index += 1
  #          k += 1
    
#    return sorted_array
from TouristPass import TouristPass
import random
def quicksort(array):
    sorted_array = array
    int num = array
    while len(array) <=1:
        return array
    else:
        q = random.choice(array)
    l_num = [n for n in num if n < q]
 
    e_num = [q] * nums.count(q)
    b_num = [n for n in nums if n > q]
    return quicksort(l_num) + e_num + quicksort(b_num)

    return sorted_array
