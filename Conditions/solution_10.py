# Problem: Recommend a type of pet food based on the pet's species and age.
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
while True:
    while True:
        try:
            species=input("Enter your pets species (Dog/Cat): ")
            age=int(input("Enter age now "))
            if species =="Dog" and age<2:
                print("Puppy food")
                break;
            elif  species =="Cat" and age>5:
                print("Senior Cat food")
                break;
        except ValueError:
            print("Enter correct value")
            continue
    response=input("Want to play again y/n")
    if response!='y':
        break;
        
