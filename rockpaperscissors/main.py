import random

def play():
    user = input("What's your choice:'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    
    # R > S, S > P, P > R
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    # R > S, S > P, P > R
    if (player == 'r' and opponent!= ('p' or 'r') ):
        return True
    
print(play())