while True:  # no need to initialize variable command before the loop starts
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
