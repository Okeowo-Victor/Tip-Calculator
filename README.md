# 
Welcome = print("Welcome to python pizza delivery  !")

Fname = input("kindly input your Name : ").capitalize()

size = input(f"hello {Fname} kindly choose your pizza Size S,M,L  :").capitalize()

cheese = input("would you like to add extra cheese? Y / N :").capitalize()

# Example 1 : payment based on there size choice
# initial bill
bill = 0
# calculate the price based on what they choose
if size == "S" :
    bill += 15
elif size =="M" :
    bill += 25
elif size =="L" :
    bill += 40
else:
    print("check again please choose between S,M, and L.")
    exit()
    
#Example 2 : Adding a bill based on Customers choices . 
if cheese =="Y":
    bill +=2
    
    # Total Bill
    print(f"Noted your final bill is: ${bill} .")
      
