age = 17

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(f"case 1:{message}")

# code from line 3 to 6 could also be written as
message = "Eligible" if age >= 18 else "Not eligible"
print(f"case 2:{message}")
