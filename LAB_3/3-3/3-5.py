data_file = open("data.csv", "r")
#Put the lines in the a list called "lines"
lines = data_file.readlines()
data_file.close()
#Open to read data.csv as f
with open('data.csv', 'r') as f:
	l = [[int(str(num)) for num in line.split(',')] for line in f]
source_file=open('data_trimed','w')
for i in l:
	#Removing the first coloumn and putting "," between them
	print(*i[1::], sep = ",",file=source_file)
