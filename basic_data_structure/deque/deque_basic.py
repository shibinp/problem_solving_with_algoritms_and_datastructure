from deque import Deque

d = Deque ()
print (d.isempty())
d.addRear(4)
d.addRear('cat')
d.addFront('dog')
d.addFront('True')
print d.items
print (d.size())
print (d.isempty())
d.addRear(8.4)
print d.items
print (d.removeRear())
print d.items
print (d.removeFront())
print d.items

