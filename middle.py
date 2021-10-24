# Write a function called middle(), that takes a list as a parameter.
# Your function should return a NEW list that contains all but the first and last elements.
# You MAY NOT use any built in methods except for .append() and len().

"""** DO NOT MODIFY BELOW **"""
#DEFINE OUR LISTS
listToMiddleOne = ['a', 'b', 'c', 'd', 'e']
listToMiddleTwo = [1,2,3,4,5]
listToMiddleThree = [True, False, True, False, True]

#INCOMPLETE FUNCTION THAT NEEDS TO BE COMPLETED
def middle(lst):#PASS LIST TO MIDDLE
    #CREATE NEW LIST BY SLICING THE OLD LIST

    t = len(lst)

    middlelst = lst[1:(t-1)]
    
    return middlelst #RETURN THE NEW LIST

"""** DO NOT MODIFY BELOW **"""

outputOne = middle(listToMiddleOne)
outputTwo = middle(listToMiddleTwo)
outputThree = middle(listToMiddleThree)


print("Before removing the first and last elements -> ", listToMiddleOne, " ,after removing -> ", outputOne)

print("Before removing the first and last elements -> ", listToMiddleTwo, " ,after removing -> ", outputTwo)

print("Before removing the first and last elements -> ", listToMiddleThree, " ,after removing -> ", outputThree)
