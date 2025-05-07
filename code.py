Lets create a game..

import random

def play():
    user=input("'R' for rock, 'P' for paper, 'S' for scissor")
    computer= random.choice(['R','P','S']) #R>P, P>S, S>R
    
    if user==computer:
        return 'Its a tie'
    if is_win(user,computer):
        return 'You won'
    
    return 'You lost'
def is_win(player,opponent):
    
    
    
    if (player=='R' and opponent=='S') or (player=='S' and opponent=='P') \
       or (player=='P' and opponent=='S'):
           return True
       
print(play())
