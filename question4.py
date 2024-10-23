# Question 4
# Create a list of five of your favourite foods. Write a python program to:
#Add two more items to the list.
#Remove one item from the list.
#Print the updated list.
my_favourite_foods=("Meat","Chicken","Pork","Gnuts","Beans")
my_favourite_foods.append("matooke")
my_favourite_foods.append("Rice")
my_favourite_foods.remove("Beans")
print("My favourite foods")

#Question 4(ii)
# Given the list of numbers =[2,5,8,10,3,6], Write a python program to:
# print the first and last elements of the list.
#print the list in reverse order.
#calculate and print the sum of all the elements in the list. 

list_of_numbers=[2,5,10,3,6]
print(list_of_numbers[:0])
print(list_of_numbers[5:]) 
print(list_of_numbers[::-1]) 
total_sum=sum (list_of_numbers)           
print(total_sum)