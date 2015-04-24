# This tests out the sort algorithm

def test():
	a = range(1,1000)
	assert sort_merge(a) == a 'Sort failed'
	b = [3,5,3,2,0,5,3,-2,3,4]
	assert sort_merge(b) == [-2,0,2,3,3,3,3,4,5,5]
	