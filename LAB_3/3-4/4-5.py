# Using recursive algorithem is the best solution for this problem

def cost(fuel,position):
	# If not at the last place than some calculation is needed    
	if position != N+1:
		Distance=D[position+1]-D[position]
		price=P[position]
		#I f there isn't enough fuel to reach the next station
		if fuel < (F * (Distance)):
			refule_cost = (C-fuel)*price + cost(C-F*(Distance),position+1)
			return refule_cost
		# If there is enough fuel to reach the next station than
		# we'll do a recursive calculation to find the minimum cost
		else:
			refule_cost = (C-fuel)*price+cost(C-F*(Distance),position+1)
			pass_cost = cost(fuel-F*(Distance),position+1)
			return min(refule_cost,pass_cost)
	else:
		return 0


#C is the capacity of the fuel tank
C = 50
#F is Fuel usage per unit of distance
F = 1
#D is the location from origin
D = [0,20,65,80,110,160]
#P is the price of fuel in each station. 0 is inculded to make the code easier to read
P = [0,10,5,3,9]
#N is Number of gas stations
N = len(D)-2

print(cost(C,0))
