stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
import random
w=["apple","ball","cat"]
choice=random.choice(w)
lives=6
lives=len(stages)-1
end=False
display=[]
for _ in range(len(choice)): #0-3
    display+="_" #diplay=display+"-"=[_]
while not end:
    guess=input("Enter your name:").lower()
    if guess in display:
        print(f"you already guessed {guess}")
    for position in range(len(choice)): #0-3
        le=choice[position] #choice[posistion] apple[0]=a ball[1]
        if le==guess:#b==b
            display[position]=le #display[0]=a

    if guess not in choice:
        print(f"you guess {guess},that not in the word you lose life")
        lives-=1
        if lives==0:
            end=True
            print("You lose")
    print(f"{''.join(display)}")
    if "_"not in display:
            end=True
            print("you win")
