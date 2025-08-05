def multiply1(x, y):
    return x*y


print("multiply1(2, 3)")
print(multiply1(2, 3))

print()
# pb is when you want to multiply more than 2 numbers together <- solution down below


def multiply2(*numbers):
    total = 1
    # numbers is called a tuple (list of objects that can not be modified)
    print(numbers)
    for number in numbers:
        print(number)
        total *= number  # total = total * number
    print(total)
    return total


print("multiply2(1, 2, 3, 4, 5)")
multiply2(1, 2, 3, 4, 5)


print()
# here is a short version of multiply2 // prints are deleted


def multiply3(*numbers):
    total = 1
    for number in numbers:
        total *= number  # total = total * number
    return total


print("multiply3(5, 6, 7)")
print(multiply3(5, 6, 7))
