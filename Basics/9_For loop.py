for index in range(3):
    print("attempt ", index + 1, (index + 1) * ".")


print()
# following lines are the same as previous code => where we specify where the range starts from, here 1 to 3, for loop stops at 4

for index in range(1, 4):
    print("attempt ", index, (index * "."))

print()
# same as previous but this time we use the step in the range
for index in range(1, 10, 2):
    print("attempt ", index, index * ".")
