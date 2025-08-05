x = 1
unitprice = 3
print("x=", x)
print("unitprice=", unitprice)

course = "Python programming"
message = """
This is a message with several lines.
The 3 " within the code (you can read them within this message)
are here to help formatting your message withing the code.
"""
print("My message reads :", message)
print(len(course))
print("course[-1]=", course[-1])
print("course[0:3] =", course[0:3])
print("course[0:] =", course[0:])
print("course[:3] =", course[:3])
print("course[:3] =", course[:])


first_name = "gerard"
last_name = "lambert"
print("first_name reads :", first_name)
print("last_name reads :", last_name)
# concatenation of strings evaluated before runtime
full_name = first_name+" "+last_name
print("concatenation first_name and last_name is :", full_name)

# formatting string does not have a constant value, it is an expression evaluated at runtimeZ
full_name = f"{first_name} {last_name}"
print("concatenation using formatting string of first_name and last_name is :", full_name)
last_name_length = f"{len(last_name)}"
print(
    f"Last name \'{last_name}\' has a length of {len(last_name)} characters.")

user_last_name = input("What is your last name? ")
print(f"Your last name has {len(user_last_name)} characters.")
