def balancer(weights):
	partial_sum=0
	whole=sum(weights)
	for i in range(len(weights)):
		partial_sum=partial_sum+weights[i]
		#print(weights[i])
		if partial_sum>=whole/2:
			return i
