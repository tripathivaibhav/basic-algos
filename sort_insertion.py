def insert(arr):

	for j in range(1,len(arr)):
		k = j-1
		key = arr[j]
		while key < arr[k] and k >= 0:
			arr[k+1] = arr[k]
			k = k -1
		arr[k+1] = key
	return arr


a = [10,9,8,7,6,5,4,3,2]
print insert(a)
	