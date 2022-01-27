#tupple
#It makes your code safer if you “write-protect” data that does not need to be changed. Using a tuple instead of a list is like having an implied assert statement that this data is constant, and that special thought (and a specific function) is required to override that.
first_tuple=("hami","96109996")
print(first_tuple)
#Tuples are immutable; you can't change which variables they contain after construction.
second_tuple=("suny","22222222")
third_tuple=("sales","3333333")

tuple_of_tuples=(first_tuple,second_tuple,third_tuple)
print(tuple_of_tuples[1][0])
