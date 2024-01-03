# Pizza Order Program
SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGE_PIZZA = 25
bill = 0
print("welcome to pizza order program")
user = input("what size pizza do you want to order? \n"
             "type 'S' for small pizza, type 'M' for medium pizza, or type 'L' for large pizza: ").lower()
if user == 's':
    bill = SMALL_PIZZA
elif user == 'm':
    bill = MEDIUM_PIZZA
elif user == 'l':
    bill = LARGE_PIZZA

add_pepperoni = input("do you want to add pepperoni type 'Y' for yes or type 'N' for no: ").lower()
if add_pepperoni == "y":
    if user == "s":
        bill += 5
    else:
        bill += 2

extra_cheese = input("do you want extra cheese type 'Y' for yes or type 'N' for no: ").lower()
if extra_cheese == "y":
    bill += 1
print(f"your total bill is {bill}rs")


# Output:
# Sample - 1
welcome to pizza order program
what size pizza do you want to order? 
type 'S' for small pizza, type 'M' for medium pizza, or type 'L' for large pizza: M
do you want to add pepperoni type 'Y' for yes or type 'N' for no: y
do you want extra cheese type 'Y' for yes or type 'N' for no: y
your total bill is 23rs

# Sample - 2
welcome to pizza order program
what size pizza do you want to order? 
type 'S' for small pizza, type 'M' for medium pizza, or type 'L' for large pizza: L
do you want to add pepperoni type 'Y' for yes or type 'N' for no: n
do you want extra cheese type 'Y' for yes or type 'N' for no: n
your total bill is 25rs
