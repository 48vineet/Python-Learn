import random

print(
    '''
 1 is for stone
 2 is for paper
 3 is for sisor
 computer is alredy selected choise

 '''
)

comp = random.randrange(1, 4)

me = int(input("Enter your choise: "))

if me == comp:
    print("Its a draw")
elif me == 1 and comp == 2:
    print("comp win he has paper")
elif me == 1 and comp == 3:
    print("you win")
elif me == 2 and comp == 1:
    print("you win")
elif me == 2 and comp == 3:
    print("comp win he has sisor")
elif me == 3 and comp == 1:
    print("you win")
elif me == 3 and comp == 2:
    print("comp win he has paper")
elif me > 3:
    print("chose no between 1 to 3")
