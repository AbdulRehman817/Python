# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. 
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit="Banana"
color=input("Enter banana color: ")
if color=="Green":
    condition="Unripe"
    print("Banana is ",condition)
elif color=="Yellow":
     condition="Ripe"
     print("Banana is ",condition)
elif color=="Brown":
     condition="Overripe"
     print("Banana is ",condition)
else:
     print("none")
