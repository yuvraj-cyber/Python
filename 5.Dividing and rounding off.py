
a = float(input("First Float: "))
b = float(input("Second Float: "))

c = a / b

print(c)

# let's suppose that we get many decimal points and we want to round off it to [3] decimal points 
print(round(a / b, 3))

#Let's round off it upto 4 decimal points 
print(round(c,4))

#Let's round off it upto 5 decimal points
print(f"{c:.5f}")