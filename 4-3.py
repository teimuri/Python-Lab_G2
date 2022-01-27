from balancer import balancer
table=[[0,1,0,1],
	[0,0,1,0],
	[1,0,1,0]]


i=len(table)#Coloumn size
j=len(table[0])#Rowe size
#List to store number of 1 in each row
rowe_weight=[]
#List to store number of 1 in each coloumn
coloumn_weight=[0]*j

for s in range(i):
	#Adding the weights of rows
	rowe_weight.append(sum(table[s]))
	for k in range(j):
		#Adding the weights of coloumns
		coloumn_weight[k]=coloumn_weight[k]+table[s][k]


print("(",balancer(coloumn_weight),",",balancer(rowe_weight),")")
