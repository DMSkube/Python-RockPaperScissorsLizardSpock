def main():
	loop = True # Option for entire program to repeat
	while loop:
		from player import Player # import class

		Tyler_Durden = Player(name='Tyler_Durden', wins = 0) # Reset Player.wins to 0 after each loop

		Marla_Singer = Player(name='Marla_Singer', wins = 0)

		match = 1 # Set to 1 instead of 0 so print statements don't begin 'match 0'
		print('\n')
		print('+'*20)
		while match < 8: # Stop after 7 matches
			print('\nIn match ', match, ', ', play(Tyler_Durden, Marla_Singer), sep='') # Calls play(). Update after each match with match number, winner, and throws.
			match += 1

		#Decide series winner
		if Tyler_Durden.wins > Marla_Singer.wins:
			print('\nTyler_Durden wins the series with an advantage of {} to {}'.format(Tyler_Durden.wins, Marla_Singer.wins)) # Print victor, count of wins-losses in series

		elif Marla_Singer.wins > Tyler_Durden.wins:
			print('\nMarla_Singer wins the series with an advantage of {} to {}'.format(Marla_Singer.wins, Tyler_Durden.wins))

		elif Marla_Singer.wins == Tyler_Durden.wins:
			print('\nThere was an even tie.')

		loop = inputValidation() # Boolean; end or repeat program


def play(Tyler_Durden, Marla_Singer):
    # Get throw from each player
    Tyler_result = Tyler_Durden.throw()
    Marla_result = Marla_Singer.throw()

# Compare results, determine victory
    # Tie game
    if Tyler_result == Marla_result:
        statement = 'there was a tie. No victory awarded.'
        return statement
        


    #Tyler_Durden Victory
    elif Tyler_result == 'rock' and (Marla_result == 'scissors' or Marla_result == 'lizard'): # Formatted for Rock-Paper-Scissors-Lizard-Spock
        statement = 'Tyler Durden wins with {} over {}.'.format(Tyler_result, Marla_result) # .format() allows multi-variable string to print as single sentence.
        Tyler_Durden.add_win() # Tally victory in Player.wins
        return statement # Will be printed in main()

    elif Tyler_result == 'scissors' and (Marla_result == 'paper' or Marla_result == 'lizard'):
        statement = 'Tyler Durden wins with {} over {}.'.format(Tyler_result, Marla_result)
        Tyler_Durden.add_win()
        return statement

    elif Tyler_result == 'paper' and (Marla_result == 'rock' or Marla_result == 'Spock'):
        statement = 'Tyler Durden wins with {} over {}.'.format(Tyler_result, Marla_result)
        Tyler_Durden.add_win()
        return statement

    elif Tyler_result == 'Spock' and (Marla_result == 'scissors' or Marla_result == 'rock'):
        statement = 'Tyler Durden wins with {} over {}.'.format(Tyler_result, Marla_result)
        Tyler_Durden.add_win()
        return statement

    elif Tyler_result == 'lizard' and (Marla_result == 'paper' or Marla_result == 'Spock'):
        statement = 'Tyler Durden wins with {} over {}.'.format(Tyler_result, Marla_result) 
        Tyler_Durden.add_win() 
        return statement


    #Marla_Singer Victory
    elif Marla_result == 'rock' and (Tyler_result == 'scissors' or Tyler_result == 'lizard'):
        statement = 'Marla Singer wins with {} over {}.'.format(Marla_result, Tyler_result)
        Marla_Singer.add_win()
        return statement

    elif Marla_result == 'scissors' and (Tyler_result == 'paper' or Tyler_result == 'lizard'):
        statement = 'Marla Singer wins with {} over {}.'.format(Marla_result, Tyler_result)
        Marla_Singer.add_win()
        return statement

    elif Marla_result == 'paper' and (Tyler_result == 'rock' or Tyler_result == 'Spock'):
        statement = 'Marla Singer wins with {} over {}.'.format(Marla_result, Tyler_result)
        Marla_Singer.add_win()
        return statement

    elif Marla_result == 'Spock' and (Tyler_result == 'scissors' or Tyler_result == 'rock'):
        statement = 'Marla Singer wins with {} over {}.'.format(Marla_result, Tyler_result)
        Marla_Singer.add_win()
        return statement

    elif Marla_result == 'lizard' and (Tyler_result == 'paper' or Tyler_result == 'Spock'):
        statement = 'Marla Singer wins with {} over {}.'.format(Marla_result, Tyler_result) 
        Marla_Singer.add_win()
        return statement
        
def inputValidation():
	while True: # Ask for input again is invalid input is given
		choice = input('\nDo you want to play again? Y or N: ')
		if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes' or choice == 'YES':
			return True

		elif choice == 'n' or choice == 'N' or choice == 'no' or choice == 'No' or choice == 'NO':
			print('Okay. Goodbye.')
			return False

		else:
			print('Invalid input! Please enter "Y" or "N".') # Ask for input again is invalid input is given

main()