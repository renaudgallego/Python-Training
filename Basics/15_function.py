def greet():
    print("Hello user")
    print("Welcome onboard")


greet()


# parameters are inputs defined for the function /below first_name and last_name are parameters
def greet_user(first_name, last_name):
    print(f"Welcome, {first_name} {last_name}")


# arguments are actual values of given parameters /below "Gérard" and "Lambert" are arguments
greet_user("Gérard", "Lambert")


greet_user("John", "Smith")
