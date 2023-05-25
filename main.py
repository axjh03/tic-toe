# importing random module
import random
#import numpy
import numpy as np
from modules import printtable,checkrow,checkcolumn

rangeFlag = 1
#table = random.sample(inputNumbers, rowAndCol**2)

while rangeFlag == 1:
    try:
        fRange = int(input("Starting Range? "))
        lRange = int(input("Ending Range? "))
        inputNumbers =range(fRange,lRange)
        rowAndCol = int(input("how many rows and column do you want to have? "))
        table = random.sample(inputNumbers, rowAndCol**2)  # non-repeating using sample() function
        rangeFlag = 0
    except:
        print("Use valid range")
    
        # fRange = int(input("Starting Range? "))
        # lRange = int(input("Ending Range? "))
        # inputNumbers =range(fRange,lRange)
        # rowAndCol = int(input("how many rows and column do you want to have? "))
        
np_table = np.array(table)
np_table_2d = np_table.reshape(rowAndCol,rowAndCol) # since we have power of 2 elements. It will be evenly distributed.

#print(np_table_2d)
printtable(np_table_2d,rowAndCol)

game_alive = True

while game_alive == True:
    choice = 0
    while choice == 0:
        choice = np.random.choice(np_table)
    usrChoice_str = str(input(f"Do you have the number {choice}?    "))
    usrChoice_str = usrChoice_str.lower()
    if usrChoice_str[0] == "y":
        indx = np.where(np_table_2d == choice)
        np_table_2d[indx] = 0
        
    if (checkrow(np_table_2d) == True):
        print("Row completed! Game Over. \n Thank You for playing this game.")
        break
    if (checkcolumn(np_table_2d) == True):
        print("Column completed! Game Over. \n Thank You for playing this game.")
        break
    
    
    printtable(np_table_2d, rowAndCol)
    print("\n")
