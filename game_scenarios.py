def player_busts(player,dealer,chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("\nPlayer wins! Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("\nDealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print('\nDealer and player tie! PUSH')
