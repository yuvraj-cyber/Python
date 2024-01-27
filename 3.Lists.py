items = ["Mia", "Sunny", "Daniel"]

print(items[0])
print(items[1])
print(items[2],"\n")

#We can also use another method
for item in items:
    print(item)

#this is to add another line for seperation between methods
print()

#Here [len()] is used to get length of the list 
for i in range(len(items)):
    print(i + 1, items[i])