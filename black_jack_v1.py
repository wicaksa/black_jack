"""A Python game of Blackjack between a user and the dealer."""

import random
from replit import clear 
from art import logo 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = True

def deal_card():
    """ Returns a random card from the deck"""
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ Takes a list of cards a calculate the score from the list"""
    if (sum(cards) == 21 and len(cards) == 2):
        return 0
    elif (11 in cards and sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

def deal_two_cards(user1, user2):
    """ Takes in two users and deals two cards to each user"""
    for i in range(2):
        user1.append(deal_card())
        user2.append(deal_card())

def show_hand_and_score(player, user_cards, user_score):
    """ Shows the user's hand and core"""
    print (f"{player} Hand: {user_cards}, {player} Score: {user_score}")

def show_computer_card(computer_cards):
    """ Shows the first card dealt to the computer"""
    print(f"CPU  Hand: [{computer_cards[0]}, 'X']")

def compare(user_score, computer_score):
    """ Compares the user score and the CPU score"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over 21. Lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else: # computer_score > user_score
        return "You lose"

# First Screen Asks User if they want to play 
print(logo)
play_game = ""
while (play_game != 'y' and play_game != 'n'):
    play_game = input("Do you want to play a game of Blackjack? 'y' or 'n': ")
if play_game == 'n':
    play_again = False
clear() 
# Game Loop
while (play_again == True):
    user_cards = []
    computer_cards = []
    is_game_over = False
    # Print Logo
    print(logo)

    # Deal two cards
    deal_two_cards(user_cards, computer_cards)

    while (is_game_over == False):
        # Calculate Score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show Cards
        show_hand_and_score("User", user_cards, user_score)
        show_computer_card(computer_cards)

        # User loop
        if (user_score == 0 or computer_score == 0 or user_score > 21):
            is_game_over = True
        else:
            user_deal = ""
            while (user_deal != "y" and user_deal != "n"):
                user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer Loop
    while (computer_score != 0 and computer_score < 17):
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Compare scores 
    show_hand_and_score("User", user_cards, user_score)
    show_hand_and_score("CPU ", computer_cards, computer_score)
    print(compare(user_score, computer_score))

    # Play Again
    restart_game = ""
    while (restart_game != 'y' and restart_game != 'n'):
        restart_game = input("Play again? 'y' or 'n': ")
    if (restart_game == 'n'):
        play_again = False
    clear()
    
# Goodbye Message
print("Goodbye.")

# End of game
