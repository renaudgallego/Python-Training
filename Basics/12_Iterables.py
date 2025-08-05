print(5)                # 5
print(type(5))          # <class 'int'>
print(range(5))         # range(0, 5)
print(type(range(5)))   # <class 'range'>
print("Python")         # Python
print(type("Python"))   # <class 'str'>

# range objects are iterables
for index in range(5):
    print(index)

print()
# str objects are also iterables
for char in "Python":
    print(char)

print()
# list objects are also iterables / list is declared with []
for element in ["apple", "banana", "coconut", "avocado", "tomato", "orange"]:
    print(element)

# you can also create your own object that are iterables
