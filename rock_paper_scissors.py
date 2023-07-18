import asci_for_rockPaperScissors
import random
# start
user_choice = int(input("what do you choose? \n type 0 for Rock, 1 for Paper or 2 for scissors'\n"))
com_hand = random.randint(0,2)
rock = asci_for_rockPaperScissors.rockAski
paper = asci_for_rockPaperScissors.paperAski
scissors = asci_for_rockPaperScissors.scissorsAski
asci_pool = [rock, paper, scissors]
# logic:

if user_choice < 0 or user_choice > 2:
    print("wrong number")
elif com_hand == user_choice:
    print("your hand: ")
    print(asci_pool[user_choice])
    print("computer's hand:")
    print(com_hand)
    print(asci_pool[com_hand])
    print("draw")

elif com_hand == 0 and user_choice == 2:
    print("your hand: ")
    print(asci_pool[user_choice])
    print("computer's hand:")
    print(com_hand)
    print(asci_pool[com_hand])
    print("You lose")
elif com_hand > user_choice:
    print("your hand: ")
    print(asci_pool[user_choice])
    print("computer's hand:")
    print(com_hand)
    print(asci_pool[com_hand])
    print("You lose")
elif user_choice > com_hand:
    print("your hand: ")
    print(user_choice)
    print(asci_pool[user_choice])
    print("computer's hand:")
    print(com_hand)
    print(asci_pool[com_hand])
    print('YOU WON')

