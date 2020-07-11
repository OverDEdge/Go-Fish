def check_game_end(go_fish_game, Players):
    if len(go_fish_game.deck) > 0:
        return False
    else:
        for player in Players:
            if len(player.hand) > 0:
                return False
            else:
                pass
        return True
