def four(arg1):
    list = []
    work = arg1.split()
    one = 0
    for i in range(len(work)):
        ones = str(work[i])
        for i in range(len(ones)):
            one += int(ones[i])
            print(one)
    list.append(one)
    return max(list)


	
result = four("15 72 80 164")
print(result)