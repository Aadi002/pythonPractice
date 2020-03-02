def maskify(cc):
    masked=""
    if len(cc) < 4:
        return cc
    else:
       for i in range(len(cc)):
           if i < (len(cc)-4):
               masked = cc.replace(cc[i],"#")
               print(masked+"",i)
    #return masked
maskify('SF$lDfgsd2eA')
#masked_num = maskify('SF$SDfgsd2eA')
#print(masked_num)
