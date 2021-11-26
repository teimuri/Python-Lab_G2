from iterator import iterator
table=[["ABCE"],["SFCS"],["ADEE"]]

row_lenght=len(table)
coloumn_lenght=len(table[0][0])
#Here in this 'for' loop every string is replaced by a series of charecters and placed inside 'new_table'
#Take note that the 'row_lenght' and 'coloumn_lenght' will remain unchanged. 
new_table=[]
for i in table:
	new_table.append(list(i[0]))

The_input=input()
answer=0	

for selected_row in range(row_lenght):
	for selected_coloumn in range(coloumn_lenght):
		if new_table[selected_row][selected_coloumn]==The_input[0]:	#If there is a match with the fist charecter of input
			answer=answer + iterator(new_table,[selected_row,selected_coloumn],The_input[1:])
	
print(answer>0)
