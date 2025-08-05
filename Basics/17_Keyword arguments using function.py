def increment(number, by):
    return number + by


print(increment(2, 1))

# line 6 can be cleary understood by another dev reading the content of the function increment
# to avoid this we can specify 'keyword arguments' like below to ease devs life
print(increment(number=2, by=1))
# or
print(increment(2, by=1))
