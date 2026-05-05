tea_varieties=['Black','Green','Oolong']
# tea_varieties[1]='Orange'
# tea_varieties.append("Green")

# for i in tea_varieties:
    # print(i,end="-")
# tea_varieties.pop() it removes the last item
# tea_varieties.remove('Oolong')

# tea_varieties.insert(3,'Orange')# here 3 is index

# tea_varieties_copy = tea_varieties  
# ['Black', 'Green', 'Oolong']
# Both variables point to the SAME list (same reference).
# If you change one, the other will also change.

tea_varieties_copy = tea_varieties.copy()  
tea_varieties_copy.append("Orange")
# ['Black', 'Green', 'Oolong', 'Orange']
# This creates a NEW list (different reference).
# Changes in one list will NOT affect the other.
