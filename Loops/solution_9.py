# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "apple","orange", "mango"]

unique_items=set()

for item in items:
    if item in unique_items:
        print("duplicate found",item)
        break
    else:
        unique_items.add(item)
