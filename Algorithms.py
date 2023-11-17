# insertion sort 
someList  = [10,9,8,7,6,5,4,3,2,1]

def insertion_sort(toSort, sortTo): 
    for i in range(1, sortTo):  #start the loop from a one offset and go onto the specified end value
        key = toSort[i]         #assign a variable to hold the satillite value from the key
        j = i - 1               #create a variable with an offset, one to the left
        while(j >= 0 and toSort[j] > key): #
            toSort[j+ 1] = toSort[j]
            j -=1
        toSort[j+1] = key 
    return toSort
print(insertion_sort(someList, len(someList)))

# find the lowest value in the list and replace it with whereever it was

def selection_sort(toSort, sortTo):
    for i in range(0, sortTo): # start a loop from 0 to the end of the list 
        lowest = i             # use the current element in the list as a comparison 
        for x in range(i, sortTo): #loop from the current element to the end of the list 
            if toSort[x] < toSort[lowest]: # compare element in nested loop to our old variable
                lowest = x                  #save the index if element is lower
        temp = toSort[lowest]               #save the lowest value 
        toSort[lowest] = toSort[i]          #overwrite whatever the lowest number is with current element
        toSort[i] = temp                    #replace the current element with the lowest value
    return toSort
    
def binary_serch(someList, target):
    left = 0
    right = len(someList)-1
    mid = (left + right) // 2
    while left <= right:
        if someList[mid] == target: return mid
        if someList[mid] > target:
            right = mid - 1
        if someList[mid] < target:
            left = mid + 1
        mid = (left + right) // 2
    return -1

print(selection_sort(someList, len(someList)))
