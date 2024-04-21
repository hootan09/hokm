#-----------------------------------------------------------
import random

# Card suit names
SUITS = ['Clubs', 'Diamonds', 'Hearts','Spades']

# Card face values
FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Define a dictionary to assign numerical values to card ranks
RANK_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Deck():
    """Represents a deck of playing cards."""

    def __init__(self):
        self.cards = []
        
        # Create all possible card combinations
        for suit in SUITS:
            for face in FACES:
                self.cards.append((face , suit))
                
    def shuffle(self):
        """Shuffles the current deck of cards."""
        random.shuffle(self.cards)
            
    def draw_card(self):
        """Draws and returns a single card from the top of the deck."""
        return self.cards.pop()
    
    def next(self, size):
        """Get the n number of cards and pop from original list"""
        hand_set = []
        for i in range(size):
            hand_set.append(self.draw_card())
        return hand_set
    
    def sort(self, unsorted_cards):
        """Sort the list first by suits in alphabetical order (suits) and then by rank values."""
        return sorted(unsorted_cards, key=lambda x: (SUITS.index(x[1]), RANK_VALUES[x[0]]))

class Player():
    """Represents a player holding a hand of cards."""
    
    def __init__(self, name='Player'):
        self.name = name
        self.hand = []
        
    def add_card(self, card):
        """Adds a single card to the player's hand."""
        self.hand.append(card)
        
    def remove_card(self, index=-1):
        """Removes and returns the specified card from the player's hand."""
        if len(self.hand) == 0 or -len(self.hand) <= index < 0:
            raise IndexError('Invalid card index. Hand empty or out-of-bounds.')
        return self.hand.pop(index)
        
    def display_hand(self):
        """Displays each card in the player's hand on its own line."""
        print(f'\n{self.name}\'s hand:')
        for i, card in enumerate(self.hand):
            print(f'{i+1}. {card}')

# def determine_winner(player1, player2):
#     """Determines which player has won the round based on their highest card."""
#     p1_high_card = max(player1.hand, key=lambda x: FACES.index(x[:-5]))
#     p2_high_card = max(player2.hand, key=lambda x: FACES.index(x[:-5]))
#     high_value = FACES.index(p1_high_card[-5:])
#     if high_value > FACES.index(p2_high_card[-5:]):
#         winner = player1
#     elif high_value < FACES.index(p2_high_card[-5:]):
#         winner = player2
#     else:
#         tiebreaker = input('\nTie breaker!\nEnter `1` to replay this round or any other number to skip it: ')
#         if int(tiebreaker) == 1:
#             determine_winner(*[player.remove_card(-1) for player in (player1, player2)])
#         else:
#             winner = None
#     return winner

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    
    # next5 = deck.next(5)
    # print(next5)
    # print(deck.sort(next5))

    print(deck.sort(deck.cards))








        