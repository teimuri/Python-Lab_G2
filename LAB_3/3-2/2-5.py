first=["ali","taheri"]
second=["babk","akbari"]
third=["hami","mehrabi"]
#List of lists
whole=[first,second,third]

print(list(whole[i][0]+' '+ whole[i][1] for i in range(len(whole))))
#List comprehension in Python is an easy and compact syntax for creating a list from a string or another list. It is a very concise way to create a new list by performing an operation on each item in the existing list. List comprehension is considerably faster than processing a list using the for loop
