import sys

class set(object):
	def __init__(self):
		self.this_list=[]
	def add(self,x):
		if x not in self.this_list:
			self.this_list.append(x)
		
	def delete(self,x):
		if x in self.this_list:
			self.this_list.remove(x)

#Finding classed by their name in strig form
def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)
# 'do_operation' will... do the operation
def do_operation(a,b,function):
	union=set()
	intersection=set()
	for i in a.this_list:
		if i in b.this_list:
			intersection.add(i)
		else:
			union.add(i)
	for i in b.this_list:
		union.add(i)
	if function=='|':
		return (union)
		
	elif function=='&':
		return(intersection)
	elif function=='==':
		return(len(intersection)==len(union))

# "operation_find" will find the operation required and the two sets being used.
def operation_find(command):
	first_set=""
	second_set=""
	operation=""
	# "condition" detemines wether a or b is being read
	condition=0
	for i in command:
		if i=='&' or i=='|' or i=='=':
			operation=operation+i
			condition=1
		elif condition==0:
			first_set=first_set+i
		elif condition==1:
			second_set=second_set+i
	return do_operation(str_to_class(first_set),str_to_class(second_set),operation)

	
		
a=set()
b=set()
a.add('hi')
b.add('no a')
c=operation_find('a|b')
c=operation_find('a&b')
print(c.this_list)
