# 2) Input time in 24-hour format and display:
# • If time < 12 → "Good Morning".
# • If 12–17 → "Good Afternoon".
# • If 18–20 → "Good Evening".
# • Else → "Good Night".

time = int(input("Enter time: "))

if(time < 12):
    print("Good morning")
elif(time >= 12 and time < 17):
    print("Good after noon")
elif(time >= 18 and time < 20):
    print("Good evening")
else:
    print("Good night")