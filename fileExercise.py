file = open("teams.txt","r")
for i in range(5):
    if i == 0 or i == 3:
        print(file.readline())
    else:
        file.readline() 

file.close()