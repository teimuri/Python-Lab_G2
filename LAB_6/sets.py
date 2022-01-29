import sys
def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)
    
def duplicate_find(a,b,function):
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
	
def operation(command):
	first_set=""
	second_set=""
	operation=""
	condition=0
	for i in command:
		if i=='&' or i=='|' or i=='=':
			operation=operation+i
			condition=1
		elif condition==0:
			first_set=first_set+i
		elif condition==1:
			second_set=second_set+i
	
	(operation)
	return duplicate_find(str_to_class(first_set),str_to_class(second_set),operation)
class set(object):
	def __init__(self):
		self.this_list=[]
	def add(self,x):
		if x not in self.this_list:
			self.this_list.append(x)
		
	def delete(self,x):
		if x in self.this_list:
			self.this_list.remove(x)
	
		
a=set()
b=set()
a.add(3)
a.add('hel')
b.add('hel')
b.add(2)
b.add(2)
f=a
c=operation("a|b")
c.add(7)
f.add(85)
f.delete('hel0')
print(f.this_list)
#print(a.this_list)
#print(b.this_list)
#print(operation("a|b"))
