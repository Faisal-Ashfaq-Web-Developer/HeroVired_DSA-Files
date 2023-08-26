num1 = [23, 34, 12, 54, 113, 65, 232]      ##1D array
matrix = [[23,43,45],[13,24,76],[63,76,677]]  ##2D array



for elements in num1:
    print(elements)

for row in matrix:
    for element in row:
        print(element)
    print()

###TO reverse the array###

newlist = []
for i in range(len(num1)-1, 0, -1):
    newlist.append(num1[i])
print(newlist)

### Palindrometest ###
palindrometest = "level"
stringArray = list(palindrometest)

newlistofarray = []
for i in range(len(stringArray)-1, -1, -1):
    newlistofarray.append(stringArray[i])
print(newlistofarray)

if newlistofarray == stringArray:
    print("Input is a palindrome")
else:
    print("input is not a palindrome")

### Fibbonacci Series ###
# fibonacci_Series = []
# def fibonacci():



## PrimeNumber ##
