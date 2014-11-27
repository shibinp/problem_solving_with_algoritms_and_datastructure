def insertion_sort(a_list):

	for index in range(1, len(a_list)):
		current_value = a_list[index]
		position = index
	while position > 0 and a_list[position - 1] > current_value:
		a_list[position] = a_list[position - 1]
		position = position - 1
	a_list[position] = current_value

a_list = [4, 5, 12, 15, 14, 10, 8, 18, 19, 20]
insertion_sort(a_list)
print(a_list)
