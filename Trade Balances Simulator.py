#Trade Imbalances Simulation
#Difference Between Exports and Imports is Trade Balance (Surplus If X-M = +, Defecit If X-M= -) 

print ("""Welcome to the Country Trade Balance Simulation! 

Please Enter the Following:
	""")

number_1 = int(input('Value of Net Exports to ROW in USD: '))

number_2 = int(input('Value of Net Imports from ROW in USD: '))

print("================================================")

print("""
Your Balance Is USD:"""), 
print( number_1 - number_2 ) 

if (number_1 - number_2) > 0: 
	print ("""
Your Country is Running a Trade Surplus!""")
	
if (number_1 - number_2) < 0:
	print ("""
Your Country is Running a Trade Defict!""")
	
if (number_1 - number_2) == 0:
	print ("""
Your Country has struck a Trade Balance!""")
	


