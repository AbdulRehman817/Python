# Problem: Movie tickets are priced based on age:
#  $12 for adults (18 and over), $8 for children.
#  Everyone gets a $2 discount on Wednesday.

day=input("Enter day ")
age=int(input("Enter your age "))
price=22
if day=="Wednesday":
    price=price-2
    print("Price for everyone is:$ ",price)
elif age>=18:
    price=12
    print("Price for adults is:$ ",price)
else:
    price=8
    print("Price for children are:$ ",price)