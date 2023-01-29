def recur(n):
	if n<1:
		return n 	
	recur(n-1)
	print("n after 1st recur: ",n)
	recur(n-1)
	print("n after 2st recur: ",n)
	return n

recur(2)
