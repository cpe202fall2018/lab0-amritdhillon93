   
def weight_on_planets():
   # write your code here
   
   # Define multipliers for different planets
   jupiter_multiplier = 2.34
   mars_multiplier = 0.38
			   
   # Ask User for input   
   user_weight = input('What do you weigh on earth? ')

   # Cast user_weight to int so I can multiply to find other weights
   user_weight = int(user_weight)
   
   # Calculate Jupiter weight and Mars weight
   jupiter_weight = user_weight * jupiter_multiplier
   mars_weight = user_weight * mars_multiplier

   print('\nOn Mars you would weigh', mars_weight, 'pounds.' + 
	'\nOn Jupiter you would weigh', jupiter_weight, 'pounds.')
	
if __name__ == '__main__':
   weight_on_planets()
