first = "reset"
second = "rest"
count = 0
while count < 5:
    for x in range(len(first)):
        for i in range(len(second)):
            if (second[i]==first[x]):
                count+= 1
                print(second[i])
                #print(count)
        
    
