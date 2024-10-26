def matrix_dot_vector(a:list[list[int|float]],b:list[int|float]) -> list[int|float]:
	c = []
	for i in a:
		# If we are sure than each element of "a" would be of the same length, this step can be ignored - instead we can check the len(a[0]) == len(b) at the start
		if (len(i) == len(b)):
			sum = 0
			for j in range(len(i)):
				sum += i[j] * b[j]
			c.append(sum)
		else:
			c = -1
			break
	return c

a = [[1,2],[2,4]]
b = [1,2]
output = [5,10]
c = matrix_dot_vector(a,b)
print(c); print(c==output)
