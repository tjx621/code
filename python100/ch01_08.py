# 冒泡排序
def bubbleSort(a):
	n = len(a)

	# i = 1
	# while i <= n-1:
	# 	j = 0
	# 	while j < n-i:
	# 		if a[j] > a[j+1]:
	# 			t = a[j]
	# 			a[j] = a[j+1]
	# 			a[j+1] = t
	# 		j += 1
	# 	i += 1

	for i in range(n-1):
		for j in range(n-i-1):
			if a[j] > a[j+1]:
				t = a[j]
				a[j] = a[j+1]
				a[j+1] = t

	for i in a:
		print(i, end=" ")
	print()

# 选择排序
def selectionSort(a):
	n = len(a)
	for i in range(0, n-1):
		for j in range(i+1, n):
			if a[j]<a[i]:
				t = a[i]
				a[i] = a[j]
				a[j] = t

	for i in a:
		print(i, end=" ")
	print()


if __name__ == "__main__":
	a = [1,3,4,2,43,5,7]
	print(a)
	bubbleSort(a)
	selectionSort(a)


