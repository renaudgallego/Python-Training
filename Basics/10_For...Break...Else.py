Successful = False

for index in range(1, 4):
    print("Attempt ", index)
    if Successful:
        print("Successful")
        break
else:  # <= this is called a for else statement
    print("Failed")
