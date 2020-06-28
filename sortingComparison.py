
import random

# https://www.geeksforgeeks.org/python-program-for-insertion-sort/

def insertionSort(arr): 

	count = 0

	# Traverse through 1 to len(arr) 
	for i in range(1, len(arr)): 
  
		key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
		j = i-1
		count += 1
		while j >=0 and key < arr[j] :
			count += 1 
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key


	return count


#--------------------------------------------------------------------------

# https://www.tutorialspoint.com/python-program-for-iterative-merge-sort

# Code for the merge subroutine

def merge(a,b):
	""" Function to merge two arrays """

	global mergeCounter
	c = []
	mergeCounter += 1
	while len(a) != 0 and len(b) != 0:
		mergeCounter += 1
		if a[0] < b[0]:
			c.append(a[0])
			a.remove(a[0])
		else:
			c.append(b[0])
			b.remove(b[0])
	mergeCounter += 1
	if len(a) == 0:
		c += b
	else:
		c += a
	return c

# Code for merge sort

def mergesort(x):
	""" Function to sort an array using merge sort algorithm """
	global mergeCounter
	mergeCounter += 1
	if len(x) == 0 or len(x) == 1:
		return x
	else:
		middle = len(x)/2
		a = mergesort(x[:int(middle)])
		b = mergesort(x[int(middle):])
		return merge(a,b)




#------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/iterative-heap-sort/#:~:text=HeapSort%20is%20a%20comparison%20based%20sorting%20technique%20where,property%20each%20time%20to%20finally%20make%20it%20sorted.


heapCounter = 0
def buildMaxHeap(arr, n):  
	global heapCounter
	for i in range(n): 
          
		# if child is bigger than parent
		heapCounter += 1  

		if arr[i] > arr[int((i - 1) / 2)]: 
			j = i  
      
			# swap child and parent until  
			# parent is smaller  
			heapCounter += 1
			while arr[j] > arr[int((j - 1) / 2)]:
				heapCounter += 1 
				(arr[j],  arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],  arr[j]) 
				j = int((j - 1) / 2) 
  
def heapSort(arr, n):  
	global heapCounter
	buildMaxHeap(arr, n)  
  
	for i in range(n - 1, 0, -1): 
          
		# swap value of first indexed  
		# with last indexed  
		arr[0], arr[i] = arr[i], arr[0] 
      
        # maintaining heap property  
        # after each swapping  
		j, index = 0, 0
          
		while True: 
			index = 2 * j + 1
              
            # if left child is smaller than  
            # right child point index variable  
            # to right child
			heapCounter += 1
			if (index < (i - 1) and arr[index] < arr[index + 1]):  
				index += 1
          
			# if parent is smaller than child  
			# then swapping parent with child  
			# having higher value  
			heapCounter += 1
			if index < i and arr[j] < arr[index]:  
				arr[j], arr[index] = arr[index], arr[j]  
          
			j = index  
			if index >= i: 
				break
  



#------------------------------------------------------------------
# Python program for implementation of Quicksort 

# https://www.geeksforgeeks.org/python-program-for-iterative-quick-sort/#:~:text=%20Python%20Program%20for%20Iterative%20Quick%20Sort%20,reduces%20below%20a%20experimentally%20calculated%20threshold.%20More%20

# This function is same in both iterative and recursive 
def partition(arr,l,h): 
	global quickCounter
	i = ( l - 1 ) 
	x = arr[h] 

	for j in range(l , h): 
		quickCounter += 1
		if arr[j] <= x: 

			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[h] = arr[h],arr[i+1] 
	return (i+1) 

# Function to do Quick sort 
# arr[] --> Array to be sorted, 
# l --> Starting index, 
# h --> Ending index 
def quickSortIterative(arr,l,h): 

	# Create an auxiliary stack 
	size = h - l + 1
	stack = [0] * (size) 

	# initialize top of stack 
	top = -1

	# push initial values of l and h to stack 
	top = top + 1
	stack[top] = l 
	top = top + 1
	stack[top] = h 

	# Keep popping from stack while is not empty 
	while top >= 0: 

		# Pop h and l 
		h = stack[top] 
		top = top - 1
		l = stack[top] 
		top = top - 1

		# Set pivot element at its correct position in 
		# sorted array 
		p = partition( arr, l, h ) 

		# If there are elements on left side of pivot, 
		# then push left side to stack 
		if p-1 > l: 
			top = top + 1
			stack[top] = l 
			top = top + 1
			stack[top] = p - 1

		# If there are elements on right side of pivot, 
		# then push right side to stack 
		if p+1 < h: 
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h 






#--------------------------------------------------------------

#This algorithm written by myself

def countSort(arr) :

	count = 0

	occurances = [0 for i in range(len(arr))]

	for number in arr :
		count += 1
		occurances[number] += 1


	startingIndeces = list()

	for i in range(len(occurances)) :
		count += 1
		startingIndeces.append(sum(occurances[:i]))
	
	sortedArr = [0 for i in range(len(arr))]

	for number in arr :
		count += 1
		sortedArr[startingIndeces[number]] = number
		startingIndeces[number] += 1

	
	return arr, count




#--------------------------------------------------------------

# https://www.geeksforgeeks.org/python-program-for-radix-sort/

# Python program for implementation of Radix Sort 

# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 
	c = 0

	n = len(arr) 

	# The output array elements that will have sorted arr 
	output = [0] * (n) 

	# initialize count array as 0 
	count = [0] * (10) 

	# Store count of occurrences in count[] 
	for i in range(0, n): 
		c += 1
		index = (arr[i]/exp1) 
		count[ int((index)%10) ] += 1

	# Change count[i] so that count[i] now contains actual 
	# position of this digit in output array 
	for i in range(1,10): 
		count[i] += count[i-1] 

	# Build the output array 
	i = n-1
	while i>=0: 
		c += 1
		index = (arr[i]/exp1) 
		output[ count[ int((index)%10) ] - 1] = arr[i] 
		count[ int((index)%10) ] -= 1
		i -= 1

	# Copying the output array to arr[], 
	# so that arr now contains sorted numbers 
	i = 0
	for i in range(0,len(arr)): 
		
		arr[i] = output[i] 

	return c

# Method to do Radix Sort 
def radixSort(arr): 
	c = 0
	# Find the maximum number to know number of digits 
	max1 = max(arr) 

	# Do counting sort for every digit. Note that instead 
	# of passing digit number, exp is passed. exp is 10^i 
	# where i is current digit number 
	exp = 1
	while max1/exp > 0: 
		c += countingSort(arr,exp) 
		exp *= 10

	return c



#--------------------------------------------------------------

sortedArray = [i for i in range(1000)]
reversedArray = [i for i in range(1000)]
reversedArray.reverse()
randomArray = [random.randint(0,999) for i in range(1000)]

print("Insertion Sort")
print("Sorted Array Operations:", insertionSort(sortedArray))
print("Reversed Array Operations:", insertionSort(reversedArray))
print("Random Array Operations:", insertionSort(randomArray))


sortedArray = [i for i in range(1000)]
reversedArray = [i for i in range(1000)]
reversedArray.reverse()
randomArray = [random.randint(0,999) for i in range(1000)]

print("Merge Sort")
mergeCounter = 0
mergesort(sortedArray)
print("Sorted Array Operations:", mergeCounter)
mergeCounter = 0
mergesort(reversedArray)
print("Reversed Array Operations:", mergeCounter)
mergeCounter = 0
mergesort(randomArray)
print("Random Array Operations:", mergeCounter)

sortedArray = [i for i in range(1000)]
reversedArray = [i for i in range(1000)]
reversedArray.reverse()
randomArray = [random.randint(0,999) for i in range(1000)]

print("Heap Sort")
heapCounter = 0
heapSort(sortedArray,1000)
print("Sorted Array Operations:", heapCounter)
heapCounter = 0
heapSort(reversedArray,1000)
print("Reversed Array Operations:", heapCounter)
heapCounter = 0
heapSort(randomArray,1000)
print("Random Array Operations:", heapCounter)



sortedArray = [i for i in range(1000)]
reversedArray = [i for i in range(1000)]
reversedArray.reverse()
randomArray = [random.randint(0,1000) for i in range(1000)]

print("Quick Sort")
quickCounter = 0
quickSortIterative(sortedArray,0,999)
print("Sorted Array Operations:", quickCounter)
quickCounter = 0
quickSortIterative(reversedArray,0,999)
print("Reversed Array Operations:", quickCounter)
quickCounter = 0
quickSortIterative(randomArray,0,999)
print("Random Array Operations:", quickCounter)



sortedArray = [i for i in range(1000)]
reversedArray = [i for i in range(1000)]
reversedArray.reverse()
randomArray = [random.randint(0,999) for i in range(1000)]

print("Count Sort")
print("Sorted Array Operations:", countSort(sortedArray)[1])
print("Reversed Array Operations:", countSort(reversedArray)[1])
print("Random Array Operations:", countSort(randomArray)[1])


sortedArray = [i for i in range(1000)]
reversedArray = [i for i in range(1000)]
reversedArray.reverse()
randomArray = [random.randint(0,999) for i in range(1000)]

print("Radix Sort")
print("Sorted Array Operations:", radixSort(sortedArray))
print("Reversed Array Operations:", radixSort(reversedArray))
print("Random Array Operations:", radixSort(randomArray))
