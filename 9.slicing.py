#Remember in python counting always start from "0",following is how the elements will be counted
#       0  1  2  3  4  5  6  7  8
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nSlicing")

print(list[2:6])
#This will give us a list of elements between "2nd" position i.e 3 and 6th position i.e 7 but the end will not be included in the sliced list.

print("\nSlice from Start")

print(list[:5])
#This will give us a list of elements between start and "5th" position i.e 6

print("\nSlice to End")

print(list[5:]) 
#This will give us a list of elements from "5th" position to end. In this case end will be included.

print("\nNegative Indexing")

print(list[-5:-1])
#we will get list of elements between "-5th" or "4th" position i.e 5 and "-1st" or "8th" position i.e 9 (9 will not be included).
