number = 100

while number > 0:
    print(number)
    number //= 2  # same as number = number // 2 <= return int value of the operation

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
