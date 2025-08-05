# LIST is declared in between square brackets []
mylist = [9, "tup", "le", 100]
print(f"This is mylist: {mylist}")

count = 0
for ele in mylist:
    print(f"ele {count}: {ele}")
    count += 1

print()

# TUPLE is declared in between parantheses ()
mytuple = (1, "li", "st", 2)
print(f"This is mytuple: {mytuple}")

count = 0
for ele in mytuple:
    print(f"ele {count}: {ele}")
    count += 1
