import random
randnumber=random.randint(1,100)
userguess=None
guesses=0

while (userguess!=randnumber):
    userguess=int(input("Enter the Guess:"))
    guesses+=1
    if (userguess==randnumber):
        print("you Guessed it right!")
    else:    
        if (userguess>randnumber):
            print("you Guessed it wrong ,Enter the smaller number")
        else:
            print("you Guessed it wrong ,Enter the larger number")   
print(f"you Guessed the number in {guesses} guesses")
with open('highscore.txt','r') as f :
    highscore=int(f.read())
if (highscore>guesses):
    print("you just broke the highscore")
    with open ('highscore.txt','w')as f:
        f.write(str(guesses))


