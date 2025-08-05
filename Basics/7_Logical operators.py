# and or not

high_income = False
good_credit = True
student = False

if high_income or good_credit:
    print("got money")
else:
    print("is broke")

if not student:
    print("not Student")
else:
    print("student")

if (high_income or good_credit) and not student:
    print("Eligible for a loan")
else:
    print("Not eligible for a loan")
