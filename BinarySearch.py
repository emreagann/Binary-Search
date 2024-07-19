def BinarySearch(array,value):
    left = 0
    right = len(array) - 1
    while left <= right:
       middle = (left + right)//2
       current = array[middle]
       if current == value:
         return middle
       if current > value:
          right = middle - 1
       else:
          left = middle + 1
    return -1
array = [3,4,7,8,11,19,25,38]
result = BinarySearch(array,11)
if result != -1:
   print("The value at index",result)