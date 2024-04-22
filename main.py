#-----------------------------------------------------------
import random
import sys
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

    def get_all_cards(self):
        return self.cards  
            
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
    def __init__(self, name='Player', is_bot= False):
        self.name = name
        self.hand = []
        self.is_bot = is_bot
        
    def add_cards(self, cards):
        """Adds a single card to the player's hand."""
        self.hand += cards
        
    def draw_card(self, index=-1):
        """Removes and returns the specified card from the player's hand."""
        if len(self.hand) == 0 or -len(self.hand) <= index < 0:
            raise IndexError('Invalid card index. Hand empty or out-of-bounds.')
        return self.hand.pop(index)
        
    def display_hand(self):
        """Displays each card in the player's hand on its own line."""
        print(self.hand, '\n')

class Game():
    """Represents a Game Manager"""
    def __init__(self):
        self.players = [Player('1'), Player('2', is_bot=True), Player('3', is_bot=True), Player('4', is_bot=True)]
        self.ruler = None
        self.trump = None
        self.round = 1
        self.table = []
        self.game_log = []
        self.deck = Deck()

    def new_round(self, trump_suit):
        """New Round"""
        self.trump = trump_suit
        self.table = []
        self.round += 1
    
    def select_trump_ruler(self, playerSize = 4):
        """Select random ruler to rule the trump"""
        ruler = random.randint(1, playerSize)
        self.ruler = int(ruler)
        return int(ruler)
    
    def select_trump_for_bot(self, cards):
        """
        the logic:
            1. Count the frequency and score of each suit (Hearts, Diamonds, Clubs, Spades).
            2. Determine the most common suit.
            3. Determine the most score suit.
            4. Return the suits base on logic in the code
        """
        # print('Ruler Bot Cards: ', cards)

        # Count the frequency of each suit (Hearts, Diamonds, Clubs, Spades)
        suit_counts = {'Hearts': 0, 'Diamonds': 0, 'Clubs': 0, 'Spades': 0}
        # Count the score of each suit (Hearts, Diamonds, Clubs, Spades)
        suit_score = {'Hearts': 0, 'Diamonds': 0, 'Clubs': 0, 'Spades': 0}
        
        for card in cards:
            suit_counts[card[1]] += 1
            suit_score[card[1]] += RANK_VALUES[card[0]]
        
        # Determine the most common suit
        most_common_suit = max(suit_counts, key=suit_counts.get)
        # Determine the most socre suit
        most_score_suit = max(suit_score, key=suit_score.get)

        if most_common_suit == most_score_suit:
            return most_common_suit
        else:
            return most_score_suit

    # def winner(self):
    #     highest_value = max(self.table, key=lambda x: x.value)
    #     winners = [player for player in self.players if highest_value in player.hand]
    #     if len(winners) > 1:
    #         return sorted(winners, key=lambda x: x.hand.index(highest_value))[0].hand.index(highest_value)
    #     else:
    #         return winners[0].hand.index(highest_value)

    # def calculate_score(self):
    #     winning_player_idx = self.winner()
    #     winning_player = self.players[winning_player_idx]
    #     score = {p: 0 for p in range(len(self.players))}

    #     # Award positive points to the winning player
    #     score[winning_player_idx] += 1

    #     # Penalize negative points for losing players
    #     losers = [p for p in range(len(self.players)) if p != winning_player_idx]
    #     qspade_count = sum([p.hand.count(Card('♠', 12)) for p in self.players])
    #     for i, l_player in enumerate(losers[:qspade_count]):
    #         score[l_player] -= 0.25

    #     self.game_log.append({"round": self.round, "scores": score})


def main():
    # ------------------- TEST SECTION --------------------------
    # deck = Deck()
    # deck.shuffle()
    
    # next5 = deck.next(5)
    # print(next5)
    # print(deck.sort(next5))

    # print(deck.sort(deck.get_all_cards()))
    # print(deck.select_random_ruler(4))
    # ----------------------------------------

    game = Game()

# while True:
    print("\nROUND {}\n".format(game.round))
    if game.round > 7:
        # break
        sys.exit(0) # the game is finished

    # Assign trump suit & deal cards
    if not game.trump:
        game.deck.shuffle()
        print('Set hand to each player (first 5 cards)\n')
        for player in game.players:
            player.add_cards(game.deck.sort(game.deck.next(5)))
        
        rulerPlayerIndex = game.select_trump_ruler(4) - 1 # start from 0
        print(f"The ruler is: player #{rulerPlayerIndex} [is a bot={game.players[rulerPlayerIndex].is_bot}]\n")
        if(game.players[rulerPlayerIndex].is_bot):
            trump_suit = game.select_trump_for_bot(game.players[rulerPlayerIndex].hand)
            # trump_suit = random.choice(SUITS)
        else:
            print(f'Player #{rulerPlayerIndex} hand:\n')
            print(game.players[rulerPlayerIndex].display_hand())
            selectedIndex = int(input(f'Player #{rulerPlayerIndex} Please Select Trump [1,5]: ')) -1
            trump_suit = game.players[rulerPlayerIndex].hand[selectedIndex][1]
        game.new_round(trump_suit)
        print("Trump suit:", trump_suit ,"\n" )

        print("Add next last 8 cards to each player\n")
        for player in game.players:
            player.add_cards(game.deck.sort(game.deck.next(8))) # max cards if 4-player game for each is 13
            player.hand = game.deck.sort(player.hand) # sorting all player hand

        print("Show all players sorted hand:\n")
        for index,player in enumerate(game.players):
            print(f"Player #{index}: ")
            player.display_hand()

    # for _ in range(4):
    #     for player in game.players:
    #         player.draw_card()

    # # Play the round
    # for rnd in range(1, 9):
    #     print("\nROUND {}, TRICK {}".format(game.round, rnd))
    #     for idx, player in enumerate(game.players):
    #         valid_cards = player.valid_cards()
    #         if not valid_cards:
    #             continue

    #         print("Player", idx + 1, "- Hand size:", len(player.hand))
    #         print("Valid cards:", [str(c) for c in valid_cards], "\n")

    #         user_input = int(input("Select a card to play (-1 to skip turn): "))
    #         selected_card = player.discard_card(user_input)

    #         if selected_card:
    #             game.table.append(selected_card)
    #             print("You played", str(selected_card))
    #             print("Table:", [str(x) for x in game.table], "\n")

    #             # Check if someone has taken the trick
    #             if len(set(game.table)) == 1:
    #                 print("Player{} wins this trick!".format(game.table[0].suit[0]))
    #                 break
    #     else:
    #         # No one took the trick yet, pick the highest card from remaining ones
    #         taking_player = game.players[idx]
    #         highest_val = max(valid_cards, key=lambda x: x.value)
    #         taking_player.hand.remove(highest_val)
    #         game.table.append(highest_val)

    #         print("No one took it, Player{} takes it automatically.".format(taking_player.hand.index(highest_val)+1))
    #         print("Table:", [str(x) for x in game.table], "\n")

    # # Determine who gets the point
    # game.calculate_score()
    # print("Current Scores:\n{}\n".format(game.game_log[-1]['scores']))


if __name__ == '__main__':
    main()










        