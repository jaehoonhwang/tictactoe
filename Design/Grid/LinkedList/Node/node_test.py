from node import Node

print('Intializing 2 classes: test1 and test2')

test1 = Node('foo', 123)
print('Return Test1')
print(test1.returnName())
print(test1.returnValue())
print(test1.returnPrev())
print(test1.returnNext())

test2 = Node('foo2', 456, test1, test1)
print('Return Test2')
print(test2.returnName())
print(test2.returnValue())
print(test2.returnPrev())
print(test2.returnNext())

print('Testing setAll()')
test1.setAll('foo_changed', 789, test2, test2)
print(test1.returnName())
print(test1.returnValue())
print(test1.returnPrev())
print(test1.returnNext())

print('Testing Access of Pointer Previous and Next')

test2_name_p = test1.returnPrev().returnName()
print('With Prev, Name: ', test2_name_p)

test2_name = test1.returnNext().returnName()
print('With Next, Name: ', test2_name)

test2_foop = test1.returnPrev()
test2_foo = test1.returnNext()
print('With test2_foop::Name: ', test2_foop.returnName())
print('With test2_foo::Name : ', test2_foo.returnName())
