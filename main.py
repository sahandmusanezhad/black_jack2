from chips import Chips
from deck import Deck
from display_cards import show_some, show_all
from game_scenarios import player_busts, dealer_busts, dealer_wins, player_wins, push
from hand import Hand
from hit_stand import hit_or_stand
from hitt import hit
from take_bett import take_bet

# Set up the Player's chips
player_chips = Chips(total=500)

while True:
    # Print an opening statement
    print("WELCOME TO BLACKJACK")

    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while True:
        # Prompt for Player to Hit or Stand and get the output
        result = hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If Player's hand exceeds 21, run player_busts() and break out of the loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        if result is False:
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches or exceeds player_hand.value
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f'\nPlayer total chips are at: {player_chips.total}')

    # Ask to play again
    new_game = input("Would you like to play again? (y/n): ").strip().lower()
    if new_game == 'y':
        continue
    else:
        print("Thank you for playing!")
        break
