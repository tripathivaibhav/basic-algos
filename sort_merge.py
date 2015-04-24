def merge(a,b):
	result = [] 
	i,j = 0,0
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			result.append(a[i])
			i = i+1
			
		else:
			result.append(b[j])
			j = j+1
			

	if i < len(a):
		#append all remaining a in to arr
		while i < len(a):
			result.append(a[i])
			i = i +1
	elif j < len(b):
		while j < len(b):
			result.append(b[j])
			j = j + 1

	return result


		
def divide(a):

	if len(a) > 1:
		#if len(a) % 2 == 0:
		st,mid = 0,len(a)/2
		#	return merge(divide(a[st:mid+1]),divide(a[mid+1:len(a)]))
		#else:
		#	st,mid = 0,len(a)/2 + 1
		return merge(divide(a[st:mid+1]),divide(a[mid+1:len(a)]))
		#print st,mid
		
	elif len(a) == 1:
		return a


a = [10,9,8,7,6,5,4,3,2]
print divide(a)
	





	