#Ask user to input 3 numbers separated by a comma 
#Split result 
#Using a for loop, calculate sum of the numbers
#Print the sum of the numbers
#Print the first number minus the second
#Print the multiplication of the third number by the first number 
#Print the sum of the numbers divided by the third number


numbers = input("Please enter three numbers separated by a comma: ").split(",")

sum=0
for number in numbers:
    sum += int(number)
print(sum)

subtraction = int(numbers[0]) - int(numbers[1])
print(subtraction)

multiplication = int(numbers[2]) * int(numbers[0])
print(multiplication)

division = sum / int(numbers[2])
print(division)



