import numpy as np

def dashes(times):
    for i in range(times):
        print("-",end = "")
    print("")
    

def printtable(list,rowandcol):
    dashes(rowandcol*6)
    for i in range(rowandcol): 
        for j in range(rowandcol):
            print(f"|{str(list[i][j]).center(4)}|", end = "")
            #dashes(28)
        print("")
        dashes(rowandcol*6)  

def checkrow(arr):
    for i in arr:
        unique_elements = set(i)
        if len(unique_elements) == 1:
            return True
        else: 
            return False

