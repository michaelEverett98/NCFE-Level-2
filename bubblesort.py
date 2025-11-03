# ==================================================
#               Sorting algorithm
#          NCFE Level 2 certificate homework
#                 Michael Everett
# ==================================================

# Bubble Sort

# Bubble sorting works by running through an array of values, comparing each one and (depending on whether you're sorting from smallest to largest or vice versa) either leaving it as be if the value is smaller, or swapping it if the value is larger. The function then iterates through the array, repeating the process, until it's been done for each value.

import random as rd

listLength = int(input("Choose a number between 0 and 20. A list will be generated with that amount of numbers and then sorted. "))
userList = []

for x in range(listLength) : # Generating a list this way allows for more thorough testing without the need to change the array in the program each time
    userList.append(rd.randint(1, 99))

print(userList) # Check the unsorted list, on the off chance it comes pre-sorted during testing
# print(listLength)

for i in range(listLength) :
    for j in range(listLength - i - 1) :
        # print(userList)
        if userList[j] > userList[j + 1] :
            userList[j], userList[j + 1] = userList[j + 1], userList[j]

# This method of sorting can actually be slightly improved by adding a boolean value to check whether or not each number has been swapped as it iterates through, and breaking the sequence each time the number isn't swapped; the version above is the more basic version of the bubble sort.

print(userList)