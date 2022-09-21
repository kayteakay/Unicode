import re


a=int(input("Enter the starting integer of the range: \n"))
b=int(input("Enter the ending integer of the range: \n"))
c=b+1

def finder(RangeStart,RangeEnd):
    list=[]
    dict={}
    for i in range(RangeStart,RangeEnd):
        binarynum=bin(i)
        list.append(binarynum)
        reg=re.search(r"[11]{2,2}",binarynum)
        if reg==None:
            dict[i]="False"
        else:
            dict[i]="True"
    print(dict)

finder(a,c)



