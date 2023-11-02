numericCode="5062 8212 3456 7892" #banc card code

numericCode=numericCode.replace(" ","")
if(len(numericCode)!=16):
    print("notCorrected")
sum=0
for i in range(0,16,2):
    sum+=(int(numericCode[i])*2-1)%9+1
for i in range(1,16,2):
    sum+=(int(numericCode[i]))

if(sum%10==0):
    print("true")   #if this card can exist
else:
    print("false")  #if this card can't exist
