def check_exam(arr1,arr2):
	total = 0
	for i in range(len(arr1)):
		if arr1[i] == arr2[i]:
			total += 4
		elif arr2[i] != "":
			total -= 1
	return total if total >= 0 else 0
