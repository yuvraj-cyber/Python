#Let's create a function to calculate Square of a number
def main():
#[def] is used to define a function and [main] is a function we have defined
    n = float(input("Enter your number to calculate Square: "))
#here we are taking float as an input from the user
    print(f"square of {n} is", square(n))



def square(n):
#Here wh have defined a function [square]
    return n**2
#[return] will return the square of n and [n**2] means n raised to the power 2 we can also use n*n

main()


#Let's Create a new function to calculate cube of a number
def cube(m):
    return m**3
m = int(input("Enter your number to calculate cube: "))
print(f"Cube of {m} is", cube(m))
