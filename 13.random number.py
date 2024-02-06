import random
#This will import the random module allowing us to generate random numbers.


while True:
#Here we are initiating an infinite loop using "while" loop.
    
    x = int(input("Enter a digit from 1 to 9: "))
    #Here we are just getting an integer as an input from the user or we can say we are prompting the user to give us digits.

    number = random.randint(1,9)
    #[randint] Random Integer. Using randint we will be generating random digits, only in this case between 1 to 9.

    if x == number:
        print(f"Great! {x} is indeed the digit.")
        break
        #If the condition is satisfied i.e if x equals to number then the loop will be terminated using [break] statement.
        #If the condition is not satisfied the loop will just continue and prompt the user again and again.
        
    if x > 9:
        print("You are crossing the line!")
    elif x < 1:
        print("You are crossing the line!")
    else:
        print("Close! Try again")
        
        