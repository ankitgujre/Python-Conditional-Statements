# 3) Create calculator
# Ex:- a=20 b=30
# a+b
# Output:- 50

print("Select any:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choose = input("Choose (1/2/3/4): ")

if choose in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choose == '1':
        print("Add = ", num1+num2)

    elif choose == '2':
        print("Subtract = ", num1-num2)

    elif choose == '3':
        print("Multiply = ", num1*num2)

    elif choose == '4':
        if num2 != 0:
            print("Divide = ", num1/num2)
        else:
            print("Error! Division by zero is not allowed.")
else:
    print("Invalid Input. Please enter 1, 2, 3, or 4.")


