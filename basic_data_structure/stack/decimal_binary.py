from stack import Stack

def divide_by_2(dec_number):
	rem_stack=Stack()


	while dec_number > 0:
		rem= dec_number % 2
		rem_stack.push(rem)
		dec_number =dec_number//2

	return rem_stack.items[::-1]


print (divide_by_2(42))
