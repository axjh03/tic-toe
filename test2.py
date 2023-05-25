import numpy as np

twoDarray = np.array([[1,4,1],[1,5,6]])
print(twoDarray)

rows,columns = np.shape(twoDarray)
print("rows", rows)
print("columns", columns)

def checkColumn(arr):
    row,column = np.shape(arr)
    for i in range(column):
        col = arr[:,i]
        unique_elements = set(col)
        if len(unique_elements)==1:
            return True
    return False

if checkColumn(twoDarray)==True:
    print("Yo")
else:
    print("No")