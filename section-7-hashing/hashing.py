import bcrypt 

pw = "Password123" 

hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode() 

given = input("Please enter a password: ") 

if bcrypt.checkpw(given.encode(), hashed.encode()): 
    print("Access granted.") 
else: 
    print("Access denied.") 