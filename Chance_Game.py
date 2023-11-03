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
          3. High Card""")
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
        
# First game
def coin_toss(account):
    print(f"""This game is simple, a 50/50 choice between "Heads" or "Tails". 
If you choose correctly you will win 85% of what you stake (The House Always Wins!), 
however, if you lose, you will lose the full bet!. Good Luck!""")
    
    if account > 0: 
        