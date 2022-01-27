import os as os
#Check to see if the path exists or make it
if not (os.path.isdir('input_files')):
	os.makedirs('input_files')
#Make the file
sourceFile = open('./input_files/python_lab.txt', 'w')
print("taha",file=sourceFile)
sourceFile.close()
