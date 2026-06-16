course = "python for beginners"
len(course)
print(len(course))
print(course.upper())
print(course[0:6])
first_name = "john"
last_name = "doe"
full_name = f"{first_name} {last_name}"
print(full_name)

x = input("Enter a number : ")
y = input("Enter another number : ")
print(f"x + y = {int(x)+int(y)}")

temperature = input("Enter the temperature in celsius : ")
if int(temperature) >= 30:
    print("its a hot day")
    print("drink plenty of water")
elif int(temperature) <= 15:
    print("its a cold day")
    print("wear warm clothes")
else:
    print("its a lovely day")
    print("great day to be outside")
print("done")

# ternary operator
age = int(input("Enter your age : "))
message = "eligible" if age >= 18 else "not eligible"
print(message)
# logical operators
has_high_income = True
has_good_credit = False
student = False
if (has_high_income or has_good_credit) and not student:
    print("eligible for loan")
else:
    print("not eligigble for the loan")

age = input("Enter your age: ")
message = "eligible" if 18 <= int(age) <= 50 else "not eligible"
print(message)
# for loop
for number in range(1, 5, 2):
    print(f"loop number {number}", (number)*".")
# for else
success = True
for number in range(1, 5):
    print(f"loop number {number}")
    if success:
        print("successful")
        break
else:
    print("loop ended without break")