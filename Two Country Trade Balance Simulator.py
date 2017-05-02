#Trade Exchange Simulator: Calculates the Trade Defecit Surplus of Two Countries

print ("""Welcome to the Two Country Trade Balance Simulation! 

Please Enter the Following:
	""")
	
number_1 = int(input("""Country A Exports to Country B: """))

number_2 = int(input("""Country B Exports to Country A: """))


if (number_1 > number_2):
	print ("""
Country A has an Account Surplus of: """)
	print (number_1 - number_2)

if (number_1 < number_2):
	print ("""
Country A has an Account Defecit of: """)
	print (number_2 - number_1)
	
if (number_1 > number_2):
	print ("""
Country B has an Account Defecit of: """)
	print (number_1 - number_2)

if (number_1 < number_2):
	print ("""
Country B has an Account Surplus of: """)
	print (number_2 - number_1)

if (number_1 == number_2):
	print ("""
Country A and B are at a Trade Equalibrium""")

	