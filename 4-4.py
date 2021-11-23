import string
#List of English alphabets
alphabet_list = list(string.ascii_uppercase)
#26 zeros to make a dictionary of alphabets
alphabet_count=[0]*26
#Dictionary of alphabets
dicte=dict(zip(alphabet_list,alphabet_count))
#Set of available alphabets and converting them into a single string to count the number of availabe alphabets
Table=[["ABCE"],["SFCS"],["ADEE"]]
Table2= list(map(lambda x,y,z:x+y+z,Table[0],Table[1],Table[2]))
#Counting and adding the number of available alphabets to the dictionary
for j in Table2[0]:
	dicte[j]=dicte[j]+1

a =input()
#Subtrac number of needed alphabets from the available ones
for j in a:
	#print "False" if the number of an alphabet reaches 0 but it is stil needed
	if dicte[j]==0:
		print("False")
		exit()
	dicte[j]=dicte[j]-1
print("True")
