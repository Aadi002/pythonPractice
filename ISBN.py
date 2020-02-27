##ISBN=list(input("Enter a valid ISBN"))
ISBN=[9,7,8,0,3,0,6,4,0,6,1,5]
oddAdds = 0
for i in range(0,len(ISBN)):
    if i % 2 != 0:
        evenAdds = ISBN[i] * 3
        oddAdds = oddAdds + evenAdds
    else:
        oddAdds = oddAdds + ISBN[i]


print(oddAdds)
finalDigit=10-(oddAdds%10)
print(finalDigit)
