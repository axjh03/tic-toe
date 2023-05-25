# Example usage
import numpy as np


arr1 = np.array([[1, 2, 3],
                 [5, 5, 5],
                 [7, 8, 9]])

arr2 = np.array([[1, 1, 1],
                 [4, 2, 4],
                 [7, 8, 9]])

x = set(('3','3','3'))
if len(x) == 1:
    print("All elements are same")
    
    
    
    
import numpy as np

def check_same_elements(arr):
    for row in arr:
        unique_elements = set(row)
        if len(unique_elements) == 1:
            return True
    return False



# Example usage
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

arr2 = np.array([[1, 2, 2],
                 [4, 4, 4],
                 [7, 8, 9]])

print(check_same_elements(arr1))  # False
print(check_same_elements(arr2))  # True

    
# We know that if x = set(('a','a','a')) then if we print(x) we only get only one a. I.e in Set data type if two element are there in a set, then all are counted as one.

