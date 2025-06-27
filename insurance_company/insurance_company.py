# ask insurance company name
name = input("Company name: ")

# ask number of employees
emp_num = input("Number of employees: ")

# ask location (city, OR country, OR state)
location = input("Location 'city', OR country, OR state': ")

# ask lowest price for a policy
low_price = input("Lowest price for a policy: ")

# ask highest price for a policy
high_price = input("Highest price for a policy: ")

# print output
print(f"We are {name} located in {location}. Our {emp_num} employees can help"
    f"you find the policy that is right for you with policies ranging from ${low_price}"
    f"to ${high_price} per month!")