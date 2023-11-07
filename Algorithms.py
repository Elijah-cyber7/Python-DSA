
someList = [9,8,7,6,5,4,3,2,1]

def insertion_sort(toSort, sortTo):
	for i in range(1, sortTo): # loop from the second element to a stopping point
		key = toSort[i]        #get a value to compare to
		j = i - 1              # get a key to a value to compare to
		while(j >= 0 and toSort[j] > key):  # while that key is not the beginning of the list and the value is greater than what we compare it to
			toSort[j+1] = toSort[j]         # shift the greater value to the right one
			j -= 1                          # compare to the next left element
		toSort[j+1] = key                   # put the value to compare against to the right of what we compare to
		print(toSort)
	return toSort

insertion_sort(someList, len(someList))