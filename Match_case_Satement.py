'''
Python match-case ek control statement hai jo ek value ko multiple patterns se compare karta 
hai. Jo pehla pattern match hota hai, uska block execute hota hai. Ye Python 3.10 me 
introduce hua aur ye C/Java ke switch-case se zyada powerful hai kyunki ye data ke parts ko 
extract bhi kar sakta hai.
'''

n = int(input("enter number: "))

def weekday(n):
    match n:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7: 
            return "Sunday"
        
print(weekday(n))