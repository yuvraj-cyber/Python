rows = int(input("Enter the number of Rows: "))
column = int(input("Enter the number of Columns: "))

#for each row in the rectangle
for i in range(rows):

    #this for each column in row
    for j in range(column):

        #This prints *
        print("*", end="")

    #This print is to add another blank line    
    print()

print()

#Lets create a square with another method
print("Creating Square")

size = int(input("Enter the size of the square: "))
for i in range(size):
    print("*" * size) 