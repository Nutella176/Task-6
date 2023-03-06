#Ask user to input three products
#Ask user to input their prices
#Split prices 
#Sum prices rounded by 2 decimal values
#Calculate average price and round by 2 decimal values
#Print 

input_products = input("Please enter the names ot three products separated by \",\": ") 
input_prices = input("Please enter the price of each product separated by \",\": ")

prices = input_prices.split(",")

sum=0
for price in prices:
    float_price = float(price)
    rounded_price = round(float_price, 2)
    #print(rounded_price)
    sum += round(rounded_price, 2)
print(sum)

average_price = round((sum / len(prices)), 2)
print(average_price)

print(f"The total of {input_products} is {sum} and the average price of the items is {average_price}")







