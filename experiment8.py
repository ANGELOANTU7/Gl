

def bubbleSort(arr):
	n = len(arr)

	swapped = False

	for i in range(n-1):

		for j in range(0, n-i-1):


			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:

			return



arr=[]
n=int(input())

for i in range (0,n):
	ele=int(input())
	arr.append(ele)

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i])

