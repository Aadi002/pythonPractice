def grades(hwork,asses,finExam):
    if (hwork or asses or finExam ) < 40 :
        print("You have failed")
    else:
        average = ((hwork+asses+finExam)/3)
        if average >= 70:
            print("you are 1st")
        elif average >=60:
            print("you are 2nd")
        else:
            print("you pass")
    return average

name = "Ben"
score1=67
score2=56
score3=77   


result = grades(score1,score2,score3)

print(name+" average is",result)
