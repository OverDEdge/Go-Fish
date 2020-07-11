GAME_PROMPT = "Do you have any: "
GO_FISH = "No! Go fish."
NO_MORE_CARDS = "No more cards in the deck. Next players turn."
VALID_CARD = "Please choose valid card from your hand"
SAVED_SET = "Player %d has gotten a full set of: %s"
HAND_EMPTY = "Hand is empty, drawing a card"

def play_turn(player1, player2, go_fish_game):

    valid_input = False
    #Check for valid input
    while not valid_input:
        player_input = str(input(GAME_PROMPT).lower())
        #remove 's' on the end if exists to make comparison easier
        if player_input[-1] == 's':
            player_input = player_input[:-1]
        else:
            pass

        card = player_input.title()

        if card in player1.hand:
            if card in player2.hand:
                player1.hand[card] += player2.hand[card]
                print("Player %d: 'Yes, I have %d'" % (player2.number, player2.hand[card]))
                del player2.hand[card]
            else:
                print(GO_FISH)
                if len(go_fish_game.deck) > 0:
                    card = go_fish_game.deck.pop()
                    if card in player1.hand:
                        player1.hand[card] += 1
                    else:
                        player1.hand[card] = 1
                else:
                    print(NO_MORE_CARDS)
            check_sets(player1, card)
            valid_input = True
        else:
            print(VALID_CARD)

def check_sets(player1, card):
    if player1.hand[card] == 4:
        player1.sets.append(card)
        print(SAVED_SET % (player1.number, card))
        del player1.hand[card]
    else:
        pass
