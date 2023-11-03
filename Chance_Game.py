import random

def welcome ():
    #In old game account = float(open("Chance_Games_Wallet").read())
    # Need to find the source of that and configure wallet
    # account = 
    print("Choose one of the following options...")
    print("""
          0. Exit
          1. Coin Toss
          2. Dice Roll
          3. Hight Card""")
    game_choice = input(">   ")
    if game_choice == "0":
        exit
    elif game_choice == "1":
        coin_toss(account)
    elif game_choice == "2":
        dice_roll(account)
    elif game_choice == "3":
        high_card(account)
    else:
        print ("Please select one of the following options...")
        print("""
          0. Exit
          1. Coin Toss
          2. Dice Roll
          3. Hight Card""")