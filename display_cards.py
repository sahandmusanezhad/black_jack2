def show_some(player,dealer):

    # dealer.card[0]
    # show only One of the Dealer's cards
    print("\nDealer's hand:" )
    print("one card hidden!")
    print(dealer.cards[1])
    # show all (2 cards) of the player's hand/cards
    print("\nPlayer's hand:" )
    for card in player.cards:
        print(card)

def show_all(player,dealer):

    # show all the Dealer's cards
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)
    # calculate and display value (J+K == 20)
    print(f"Value of the Dealer's hand is: {dealer.value}")

    # show all the players cards
    print("\n Player's hand:")
    for card in player.cards:
        print(card)
    print(f"Value of the Player's hand is: {player.value}")