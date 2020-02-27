biology = float(input("Enter your marks obtained in Boilogy: "))
chemistry = float(input("Enter your marks obtained in Chemistry: "))
physics = float(input("Enter your marks obtained in physics: "))
if biology < 40:
    print("Sorry,failed")
elif chemistry < 40:
    print("Sorry,Failed")
elif physics < 40:
    print("you have failed")
else:
    score = ((biology+chemistry+physics)/3)
    if score >= 70:
        print("yayiee,you are first in rank!!")
    elif score >=60:
        print("you got 2.1!!")
    elif score >=50:
        print("you got 2.2!!")
    elif score >=40:
        print("you pass")

