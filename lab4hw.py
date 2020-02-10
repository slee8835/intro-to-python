
##1
def fred():
        jane()
        print ("Zap")

def jane():
        print ("ABC")

jane()		#ABC
fred()		#ABC Zap
jane()		#ABC


##2
#pathogens = ['MRSA', 'E.coli', 'C.difficile']
#for bacteria in pathogens:
#        doubling_time = float(input("What is the doubling time in hours of " + bacteria+"? "))
#        population = 2** (int(24/doubling_time))
#        print ("In 24 hours, the population of "+ bacteria+" will go from 1 to " + str(population) )
#print ('Done!')

##write a function for the code above

def patho_double():
	"""
	this function is used to calculate the population of 
	the following pathogens- MRSA, E.coli and C.difficule.
	Users can input the doubling time of each pathogen in
	order to calculate the population in 24 hours.
	"""
	pathogens = ['MRSA', 'E.coli', 'C.difficile']

	for bacteria in pathogens:
		doubling_time = float(input("What is the doubling time in hours of "+ bacteria +"? "))
		population = 2** (int(24/doubling_time))
		print ("In 24 hours, the population of "+ bacteria+" will go from 1 to " + str(population) )

	return str("Done!")


status = patho_double()
print(status)