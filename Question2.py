# 2) Take a variable with a numeric grade and output the corresponding letter grade

def grade_check (Grade_input):
    if Grade_input < 50:
        print("You got a F")
    elif Grade_input >= 50 and Grade_input < 60:
        print("You got a D")
    elif Grade_input >= 60 and Grade_input < 70:
        print("You got a C") 
    elif Grade_input >= 70 and Grade_input < 80:
        print("You got a B")
    elif Grade_input >= 80 and Grade_input <= 100:
        print("You got an A")
    else:
        print("Please input your real grade")
    return grade_check

x = 2
while x < 3:
    Grade_input = float(input("Please input your numeric grade: "))
    print (grade_check(Grade_input))