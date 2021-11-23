import os
os.system("touch test.py")
#Opening the file
sourceFile = open('test.py', 'w')
#print "Taha" to file
print("taha",file=sourceFile)
#Close file
sourceFile.close()
#Using "with" and adding text
with open('test.py','a') as sourceFile:
	sourceFile.write('hello')
