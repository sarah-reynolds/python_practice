# print "Sarah Basinger"

name = "Sarah Basinger"
name = "Sarah " + "Basinger"
forty_two = 40 + 2
# print forty_two
forty_two = 84 / 2
# print forty_two

animals = ['wolf','giraffe','hippo']
# print animals
# print animals[0]
# print animals[-1]
animals.append('alligator')
# print animals
animals.remove('wolf')
# print animals
animals.insert(0,'zebra')
# print animals
animals[0] = 'horse'
# print animals
animals.pop()
# print animals


dc_class = "Michael, Paul, Mason, Casey, Connie, Sarah, Andy"
dc_class_as_array = dc_class.split(', ')
print dc_class_as_array
# print sorted(dc_class_as_array)
# print dc_class_as_array
dc_class_sorted = sorted(dc_class_as_array)
# print dc_class_sorted
dc_class_as_array.reverse()
# print dc_class_as_array
# print len(dc_class_as_array)
# print dc_class_as_array[2:4]
# for student in dc_class_as_array:
	# print student
# for i in range(1,10):
	# print i
# for i in range(1,len(dc_class_as_array)):
	# print dc_class_as_array[i]


def say_hello():
	print 'hello, world'
# say_hello()

def say_hello_with_name(name):
	print "hello, " + name
say_hello_with_name('Sarah')


first_name = "Sarah"
last_name = "Basinger"
print "Hello {} {}".format(first_name, last_name)
print "Hello %s %s %d" % (first_name, last_name, 3)

