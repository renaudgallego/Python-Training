x = input("x=")
y = input("y=")
print(type(x))
z = float(x)+float(y)
print(f"x = {x}, y = {y}, z = x + y = {z}")

# Fonctions to convert into specific type
# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy values in Python:
# 0
# "" => empty string
# None
# so converting those falsy value into boolean will lead to False otherwise it will be True
print()
print(f"bool(0)= {bool(0)}")
print(f"bool(None)= {bool(None)}")
print(f"bool(\"\")= {bool("")}")
print()
print(f"bool(0.000001)= {bool(0.000001)}")
print(f"bool(\"None\")= {bool("None")}")
print(f"bool(\"False\")= {bool("False")}")
