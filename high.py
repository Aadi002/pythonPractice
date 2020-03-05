def four(arg1):
    list = []
    work = arg1.split()
    for i in range(len(work)):
        ones = str(work[i])
        one = int(ones[0]) + int(ones[1])
        list.append(one)
    return max(list)


	
result = four("15 72 80 164")
print(result)