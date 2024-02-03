import statistics
#This will import the "statistics" module which can be used to perform different statistical operations such as mean, median, etc.

marks = input("Enter your marks seperated by spaces: ")
#prompting user to provides the marks seperated by spaces and storing them into variable "marks"

list = [int(item) for item in marks.split()]
#Now creaating a [list] of the marks given by the user.
#[marks.split()] splits the input into a list based on spaces

average = statistics.mean(list)
#this will calculate mean/average using the [statistics.mean()] function and stores it into "average" variable

print(list)
print(average)
