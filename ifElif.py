# if elif else

num1 = int(input("Enter your marks: "))


if(num1 >= 80 and num1 <= 100):
    print("Grade A")
elif(num1 >= 60 and num1 < 60):
    print("Grade B")
elif(num1 >= 30 and num1 < 60):
    print("Grade c")
elif(num1 >= 0 and num1 < 30):
    print("Grade D")
else: 
    print("invalid")