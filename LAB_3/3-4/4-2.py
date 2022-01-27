from collatzer import collatzer
from collatzer import collatzer2
import time
n=1001
#Using time to mesure performance
start_time = time.time()
#List of the series for the the given number
listof=[]
#List of numbers to try
number_list=list(reversed(range(1,n)))
i=0
maximum=0

for i in number_list:
	#Number list is used to remove numbers already seen in the previous series
	(r,null,number_list)=collatzer(i,[],number_list)
	#Finding the maximum
	if r>maximum :
		listof=null
		maximum=r


print("--- %s seconds ---" % (time.time() - start_time))
print(listof)


#The same code as above but without previously seen numbers annihilation
#which results in less efficient code
start_time = time.time()
listof=[]
number_list=list(reversed(range(1,n)))
number_list.remove(5)
maximum=0
for i in number_list:
	(r,null)=collatzer2(i,[])
	if r>maximum :
		listof=null
		maximum=r
#print

print("--- %s seconds ---" % (time.time() - start_time))
