# optional parameters need to be declared after the required parameters
# here required parameter is number, optional parameter is by
def increment(number, by=1):
    return number + by


print(increment(2))
print(increment(2, by=2))
