import random #importing the random module for generating random numbers

hands = ['rock', 'scissors', 'paper'] # variable which store the hand choices possible for playing game and results

#Dictionary wich map game results to corresponding messages.
results = {
    'Win!': 'you win!',
    'Lose!': 'you lose!',
    'Draw': 'draw try again'
}

def get_message():
#displaying starting game message
    print("Start 'rock-paper-scissors' game")

def get_player_hand():
    while True:  # Keep asking for input until a valid one is provided
        try:
            print("Input your hand choice")  # Input message to prompt user to input their hand
            input_message = ''
            for index, hand in enumerate(hands):  # Constructing the hand option message
                input_message += f"{index}: {hand}"
                if index < len(hands) - 1:
                    input_message += ', '
            player_choice = int(input(input_message))  # Attempt to convert input to integer

            if 0 <= player_choice < len(hands):  # Check if the input is a valid hand choice
                return player_choice  # Return the valid hand choice
            else:
                print("Invalid choice. Please choose a number between 0 and 2.")
        except ValueError:  # Catch the ValueError if the input is not an integer
            print("Invalid input. Please enter a number.")


def get_computer_hand(): #function to generate the random handchoice for computer
    return random.randint(0, 2) # choosing random numbers between 0 nd 2

def get_hand_name(hand_number): # function for returning hand name for corresponding given index

    return hands[hand_number]

def view_hand(your_hand, computer_hand): # function to display hand name choosen by each player
    print('My hand is ' + get_hand_name(your_hand))
    print("Computer's hand is " + get_hand_name(computer_hand))

def view_result(hand_difference):# a function used to judge and determine who wins and the one who loses
    if hand_difference == 0:
        return 'Draw' # if the the hand fiffence is 0 the game result is 'Draw'
    elif hand_difference in [-1, 2]:
        return 'Win!'#if the hand diference is between -1 and 2 the the user Win!
    else:
        return 'Lose!' # otherwise user lose!

def give_results(result):#displaying the result message deping on game results
    print(results[result])

def play():#main function for playing game and repeating antile there is a win or lose
    get_message()#Displaying the starting message

    while True:
        your_hand = get_player_hand() #get player's  hand
        computer_hand = get_computer_hand()# get computer's hand

        hand_difference = your_hand - computer_hand# calculating the difference between hand choice coosen by the player nad computer

        view_hand(your_hand, computer_hand) # display the hands
        result = view_result(hand_difference)# determine the results
        give_results(result)#display the results message

        if result != 'Draw': #if the result not 'Draw' break the loop
            break

def main():
    play()#call function to play the game

# Run the game
main() #start the game