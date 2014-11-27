from stack import Stack

r_stack = Stack()

def to_str(n,base):
	converting_string= "01234356789ABCDEF"
	while n > 0 :
		if n < base:
			r_stack.push(converting_string[n])
		else:
			r_stack.push(converting_string[n%base])
		n= n // base
		res = ""
	while not r_stack.is_empty():
		res = res+str(r_stack.pop()
	return res



print (to_str(1453,16))
		

