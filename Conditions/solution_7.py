# Problem: Check if a password is "Weak", "Medium", or "Strong".
#  Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


password="Hello"

if len(password)<6:
    print("Password is weak")
elif len(password)>6 and len(password)<10:
    print("Password is medium")
else:
    print("password is strong") 