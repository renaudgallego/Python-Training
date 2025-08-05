# age should be between 18 and 65
age = 27


if age >= 18 and age < 65:
    print("Eligible")
else:
    print("Not eligible")

if 18 <= age < 65:
    print("Eligible")
else:
    print("Not Eligible")

# here is the best way to  write it
message = "Eligible" if 18 <= age < 65 else "Not eligible"
print(message)
