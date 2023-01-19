import random
print("Welcome to Guesser Game\n This game has 5 Levels")
print("LEVEL 1")
n=random.randint(0,1)
#print(n)
print("Guess the number between 0 and 1")
m=int(input())
if(m==n):
    print("Congrats You passed Level 1")
    n=random.randint(0,5)
    #print(n)
    print("Guess the number between 0 and 5")
    m=int(input())
    if(m==n):
        print("Congrats You passed Level 2")
        n=random.randint(0,10)
        #print(n)
        print("Guess the number between 0 and 10")
        m=int(input())
        if(m==n):
            print("Congrats You passed Level 3")
            n=random.randint(0,15)
            #print(n)
            print("Guess the number between 0 and 15")
            m=int(input())
            if(m==n):
                print("Congrats You passed Level 4")
                n=random.randint(0,20)
                #print(n)
                print("Guess the number between 0 and 20")
                m=int(input())
                if(m==n):
                    print("Congrats You passed Level 5")
                    print("YOU WON THE GAME :)    YOU ARE A REAL GUESSER")
                else:
                    print("Oops So Close \nFailed :| Better luck next time")
            else:
                print("Ahh you were right there\nFailed :| Better luck next time")
        else:
            print("Dont loose hope\nFailed :| Better luck next time")
    else:
        print("Today is not your day\nFailed :| Better luck next time")
else:
    print("Very Bad luck to be Honest\nFailed :| Better luck next time")