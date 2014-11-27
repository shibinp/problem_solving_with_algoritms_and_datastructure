def list_sum(num_list):
	total_sum= 0
	for i in num_list:
		total_sum=total_sum + i
	return total_sum

print list_sum([100,200,300])
