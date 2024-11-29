def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("Enter the chips bet: "))
        except ValueError:
            print("Please enter a number.")
        else:
            if chips.bet > chips.total:
                print(f'sorry, you do not have enough chips! you have: {chips.total}')
            else:
                break