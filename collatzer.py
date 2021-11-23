def collatzer(n,listof,number_list):
	#All of this is basicly the 
	r=0
	#Adding the current number to store the series
	listof.append(n)
	if n <=len(number_list):
		number_list[len(number_list)-int(n)]=1
	if n==1:
		return (r,listof,number_list)
	if n%2==0:
		(a,listof,number_list)=collatzer(n/2,listof,number_list)
		r=a+1
	if n%2==1:
		(a,listof,number_list)=collatzer(3*n+1,listof,number_list)
		r=a+1
	
	return (r,listof,number_list)
	
def collatzer2(n,listof):
	
	r=0
	listof.append(n)
	if n==1:
		return (r,listof)
	if n%2==0:
		(a,listof)=collatzer2(n/2,listof)
		r=a+1
	if n%2==1:
		(a,listof)=collatzer2(3*n+1,listof)
		r=a+1
	
	return (r,listof)
