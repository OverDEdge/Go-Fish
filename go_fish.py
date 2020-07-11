#CARDS = ['King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five',
#        'Four', 'Three', 'Two', 'Ace']
CARDS = ['Ace', 'King', 'Queen', 'Jack', 'Ten']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
DECK_OF_CARDS = []
NUMBER_OF_START_CARDS = 5
player_one = []
player_two = []
# 's' is not considered numeric so can assign the input variables to that
# to get correct numeric input
nr_of_players = 's'
PLAYER_PROMPT = "How many players in the game ({} - {}): "
CURRENTLY_PLAYING = "Currently playing: Player %i"
ASK_PLAYER=  "Which player do you want to ask? {} \n"
NEXT_PLAYER = "Ready for next player?\nPress enter to continue..."
game_ended = False
MAX_PLAYERS = 5
MIN_PLAYERS = 2

from random import shuffle
from itertools import cycle
import player
import os
from play_turn import *
from check_game_end import *

class Game:
    def __init__ (self):
        self.deck = []

# One line nested for loop that creates and ordered deck of cards "King of Hearts"...
#[[DECK_OF_CARDS.append(card + ' of ' + suit) for suit in SUITS] for card in CARDS]
[[DECK_OF_CARDS.append(card) for suit in SUITS] for card in CARDS]

go_fish_game = Game()

#Shuffle the deck of cards
go_fish_game.deck = DECK_OF_CARDS
shuffle(go_fish_game.deck)

while not nr_of_players.isnumeric():
    nr_of_players = input(PLAYER_PROMPT.format(MIN_PLAYERS, MAX_PLAYERS))

if int(nr_of_players) > MAX_PLAYERS:
    print("Number of players set to Max = %d" % MAX_PLAYERS)
    nr_of_players = MAX_PLAYERS
elif int(nr_of_players) < MIN_PLAYERS:
    print("Number of players set to Min = %d" % MIN_PLAYERS)
    nr_of_players = MIN_PLAYERS
else:
    pass

nr_of_players = int(nr_of_players)
Players = [None]*nr_of_players

for i in range (0, nr_of_players):
    Players[i] = player.Player(i + 1)
    for _ in range(0, NUMBER_OF_START_CARDS):
        card = go_fish_game.deck.pop()
        if card in Players[i].hand:
            Players[i].hand[card] += 1
            check_sets(Players[i], card)
        else:
            Players[i].hand[card] = 1
    #print("Player %i starting hand: " % (i+1), Players[i].hand)

while not game_ended:
    for player in cycle(Players):
        input(NEXT_PLAYER)
        os.system('cls')
        ask_player = 's' # set so that numeric is evauated as False
        # Print currently playing player
        print(CURRENTLY_PLAYING % player.number)
        print("Player hand is:", player.hand)
        if len(player.hand) == 0:
            print(HAND_EMPTY)
            if len(go_fish_game.deck) > 0:
                card = go_fish_game.deck.pop()
                player.hand[card] = 1
        else:
            other_players = list(range(1, len(Players) + 1))
            other_players.remove(player.number)
            if len(other_players) > 1:
                while not ask_player in other_players:
                    ask_player = 's' # set so that numreic is evauated as False
                    while not ask_player.isnumeric():
                        ask_player = input(ASK_PLAYER.format(other_players))
                    ask_player = int(ask_player)
                    if not ask_player in other_players:
                        print("Please choose valid player")
            else:
                ask_player = other_players[0]
            play_turn(player, Players[ask_player - 1], go_fish_game)
        if check_game_end(go_fish_game, Players):
            game_ended = True
            break

print("Game has ended!")
winning_player = Players[0]
winners = []
for player in Players:
    print("Player %d has %d number of sets." % (player.number, len(player.sets)))
    if len(player.sets) > len(winning_player.sets):
        winners = [player]
        winning_player = player
    elif len(player.sets) == len(winning_player.sets):
        winners.append(player)
    else:
        pass

print("The winner is Players are:")
for player in winners:
    print(f'Player {player.number}')
