
#Creation of a stock pricing program
#initialize the count variable to 0
count = 0
#initialize the sum variable to 0
total_sum = 0
#input full_name
full_name = str(input("What is your name: "))
#input the min_price and convert it to float
min_price = float(input("What is the minimum price "))
#create a list of prices example: price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8,
#79.3, 101.2]
price_list = [69.10, 71.50, 84.45, 91.50, 67.84, 81.22, 84.64, 58.88,
79.30, 101.21]

#for price in price_list
for price in price_list:
#add current price to sum
    total_sum += price
#if price > min_price
#increment count by 1
    if price > min_price:
        count += 1

#output "Hello",name,"the minimum price is ",min_price
#output "There are ",count,"prices greater than the minimum price"
#output "The total price is ",sum
print("Hello",full_name, "the minimum price is ",min_price)
print("There are",count,"prices greater than the minimum price")
print("The total price is ", total_sum)
