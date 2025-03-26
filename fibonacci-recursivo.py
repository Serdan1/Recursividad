def fibonacciR(n):
	if n == 0 or n == 1:
		return n
	else:
		return fibonacciR(n-1) + fibonacciR(n-2)

print(fibonacciR(10))