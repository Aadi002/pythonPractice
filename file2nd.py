file = open("teams1.txt","r+")
lines=file.readlines()
print(lines)

lines[0]="This is a new line\n"

for i in range(len(lines)):
    print(lines[i])

file.close()



#lines[0]="This is a new line"

#print(file.readlines())