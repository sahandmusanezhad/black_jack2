from hitt import hit


def hit_or_stand(deck, hand):
    x = input("\nDo you want to hit or stand (h/s): ").strip().lower()
    if x == 'h':
        hit(deck, hand)
        return True  # Player hits
    elif x == 's':
        print("Player stands. Dealer's turn.")
        return False  # Player stands
    else:
        print("Invalid input. Please enter 'h' or 's'.")
        return True
