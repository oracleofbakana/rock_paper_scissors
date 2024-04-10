import random
print("Welcome to Rock, paper and Scissors game with the Computer\n")
rockImage = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                    '''
paperImage = '''
                            
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|    
'''

scissorsImage = """

    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
"""

gameImages = [rockImage, paperImage, scissorsImage]
rock = 0
paper = 1
scissors = 2

userChoice = int(input("Enter any digit between 0 and 2 to play now\n"))
computerChoice = random.randint(0,2)
print("Computer Choice: ")
print(gameImages[computerChoice])

print("You chose:")

if userChoice >= 3 or userChoice < 0:
    print("You chose an invalid number. You lost")
else:
    print(gameImages[userChoice])
    if userChoice == 0 and computerChoice == 2:
        print("You Won")
    elif computerChoice == 0 and userChoice == 2:
        print("You lost.")
    elif computerChoice > userChoice:
        print("You lost")
    elif userChoice > computerChoice:
        print("You lost")
    elif userChoice == computerChoice:
        print("Its a draw")


