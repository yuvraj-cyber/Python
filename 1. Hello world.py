#1
name = input("1: What's your name?")
# Here 'name' is a variable and we use 'input' to get data(here name) from user
 
 #2
print("2: Hello," +" " + name)
# Here we use 'print' to get output and 'name' is the variable and it will give output what ther user has given us
 
#3
print(f"3: Hey, {name}") 
# here "f" represents special clue

#4
print("4:\"Hi\"")
# here we use "\" to get quotes (") in output

#5
name = name.strip()
# Remove white spaces or space to the right or left of input
print("5:" + name)

#6
name = name.capitalize()
# it Makes the first letter of first word capital
print('6:',name)

#7
name = name.title()
# it Makes the first letter of every word capital
print('7:',name)

#8
name = name.upper()
# it Makes the every letter of every word capital
print('8:',name)

#9
name = name.lower()
# it Makes the every letter of first word smaller
print('9:',name)
