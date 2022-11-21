'''
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
'''

import random

# Each card is represented as a number, 11 can turn into 1 when needed
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Used to print the values so the uses knows what the dump is going on
def show_hands(full=False):
    # full is for printing the entire dealer hand
    if not full:
        print("Dealer's first card:", dealer_cards[0])
        print("Your cards:", player_cards, f"equals to {sum(player_cards)}")
    else:
        print("Dealer's cards:", dealer_cards, f"equals to {sum(dealer_cards)}")
        print("Your cards:", player_cards, f"equals to {sum(player_cards)}")


# Used for printing the final scores and deciding who won
def results():
    show_hands(full=True)

    dealer_total = sum(dealer_cards)
    player_total = sum(player_cards)

    if dealer_total > player_total:
        print("You lost!")
    elif dealer_total < player_total:
        print("You won!")
    else:
        print("Draw!")


# The while loop for a whole game of blackjack
# Player and dealer are dealt two cards
# Ask to hit or stand
# In case of player overflow, lose automatically
# If the bot has less than 17, give him a new card
# In case of dealer overflow, win automatically
p_again = "y"
while p_again != "n":
    # Reset hands
    player_cards, dealer_cards = [], []

    # Deal
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))

    # double 11 prevention
    if sum(player_cards) > 21:
        player_cards[0] = 1

    if sum(dealer_cards) > 21:
        dealer_cards[0] = 1

    show_hands()

    # In case of overflow, one of the variables below (lost, won) turns True and the cycle variable turns false,
    # so it doesn't run again. won and lost are needed not to print the result two times
    lost = False
    won = False
    cycle = True
    # The "Hit Stand" cycle
    while cycle:
        # The almighty question
        decision = input("hit or stand?\n")
        if decision == "hit":
            player_cards.append(random.choice(cards))
            # Checks if an overflow happened, it also checks if the player has an 11 card because if he has one,
            # it turns into 1 and the overflow is cancelled
            if sum(player_cards) > 21 and 11 not in player_cards:
                show_hands(full=True)
                print("You lost the game!")
                lost = True
                cycle = False
            elif 11 in player_cards:
                for i, num in enumerate(player_cards):
                    if num == 11:
                        player_cards[i] = 1
                        break
                show_hands()
            else:
                show_hands()

        elif decision == "stand":
            # Rules explain this
            while sum(dealer_cards) < 17:
                dealer_cards.append(random.choice(cards))
                # Checks if an overflow happened, it also checks if the dealer has an 11 card because if he has one,
                # it turns into 1 and the overflow is cancelled
                if sum(dealer_cards) > 21 and 11 in dealer_cards:
                    for i, num in enumerate(dealer_cards):
                        if num == 11:
                            dealer_cards[i] = 1
                            break
                elif sum(dealer_cards) > 21 and 11 not in dealer_cards:
                    show_hands(full=True)
                    print("You won!")
                    won = True
            # When a stand happens the cycle ends automatically
            cycle = False
        decision = ""

    # In case of overflow, this is False
    # else, print the results
    if not lost and not won:
        results()

    p_again = input("Play again? (y/n)\n")
