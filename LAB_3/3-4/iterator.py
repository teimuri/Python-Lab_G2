def iterator(table,location,target):
#---------Parameters
# 'table' is the table of availabe charecters
# 'location' indicate the location of the array which is the end of the root.
# that has been made until now from privious iterations.
# 'target' Is the target string which a root needs to be found for
#-------------------

	# The array of the current location is turned to 0 to indicate 
	#that this array has been used in the root so not to cross it again
	table[location[0]][location[1]]=0	

	row_lenght=len(table)
	coloumn_lenght=len(table[0])
	
	if(0==len(target)):	#Obviously if the lenght of the 'target' is 0, then we have reached the end of the iterations and the search has been sucessful
		return 1
	
	
	for nearby_locations in ([location[0]-1,location[1]],
							[location[0]+1,location[1]],
							[location[0],location[1]-1],
							[location[0],location[1]+1]):
		if (nearby_locations[0] in range(row_lenght)) and (nearby_locations[1] in range(coloumn_lenght)):
				if table[nearby_locations[0]][nearby_locations[1]]==target[0]:
					if (iterator(table,nearby_locations,target[1:])):

						return 1
	return 0
								
