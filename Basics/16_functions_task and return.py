# function that performs a task
def greet(name: str):
    print(f"Hello, {name.capitalize()}!")

# function that returns a vaalue


def get_greetings(name: str):
    return f"Hi, {name.capitalize()}!"


greet("steve")
print(get_greetings("renaud"))


# example of function that returns a value
message = get_greetings("sAm")  # <-- this one return a string as value
# <-- this one returns a file as value
file = open("HelloWorld\\16_functions_task and return_filecontent.txt", "w")
file.write(message)
file.close()


# another example of function that returns the value (content of a py file)
file2 = open("HelloWorld\\16_functions_task and return.py", "r")
print(f"Content of : {file2.name}")
print(file2.read())
file2.close()


# FYI function that performs a task returns None
# Jean-michel est affiché suivi d'une nouvelle ligne contenant None
print(greet("jean-michel"))
