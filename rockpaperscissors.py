import random

def play():
    x = 0

    while(x !=  100):
        user = input("'p' for paper, 'r' for rock, 's' for scissors: ")
        user.lower()
        computer = random.choice(['r', 'p', 's'])
        
        if user == computer:
            return "You both chose {}. It is a tie".format(computer)
        
        if choose(user, computer):
            x +=1 
            return "You chose {} and the computer chose {}. You win!".format(user, computer)

        return "You have chose {} and the computer has chosen {}. You lost".format(user, computer)
   

    
def choose(user, computer):
    if (user=='s' and computer=='p') or (user== 'p' and computer=='r') or (user=='r' and computer=='s'):
        return True 
    return False

if __name__ == '__main__':
    print(play())
