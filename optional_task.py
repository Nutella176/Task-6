#Ask user to input length of each side of the triangle one by one
#Calculate semi permeter 
#Calculate area 
#Print area 

side1 = float(input("Please enter the length of the first side of the triangle: "))
side2 = float(input("Please enter the length of the second side of the triangle: "))
side3 = float(input("Please enter the length of the third side of the triangle: "))
semi_perimeter = (side1 + side2 + side3) / 2
area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5
print(area)

