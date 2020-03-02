file = open("existFile.txt","r")
outfile=""
for line in range(10):
    if line % 2 == 0 :
        outfile = outfile + file.readline()
    else:
        file.readline()

file = open("existFile.txt","w")
file.write(outfile)
file.close()

file = open("existFile.txt","r")
lines = file.readlines()
lines = "".join(lines)
print(lines)