from itertools import combinations
def main():
    file_name="data/eigenValues.txt"
    f = open(file_name,"r")
    d = f.readlines()
    inputList=[x.split() for x in d]
    for i in range(0,len(inputList)):
        inputList[i]=float(inputList[i][0])
    
    mainList=[]
    i=0
    while i<len(inputList):
        mainListPart=[]
        mainListPart.append(i+1)
        mainListPart.append(inputList[i])
        mainList.append(mainListPart)
        i=i+1
    
    mainList=sorted(mainList, key=lambda x: x[1],reverse=True)
    topX=14
    maxOrder=10
    
    FI=[]
    FI,val=generateFI(mainList,topX,maxOrder)
    
    for i in range(0,len(FI)):
        print("-------------------------------------------------\nFrequent ItemSets of order ", i+1)
        print(FI[i])
        print(val[i])
        
def generateFI(order1,x,mo):
    order1=order1[:x]
    orderMat=[]
    FIMain=[]
    valMain=[]
    order1FI=[]
    value1FI=[]
    for i in range(0,len(order1)):
        order1FI.append(order1[i][0])
        value1FI.append(order1[i][1])    
    FIMain.append(order1FI)
    valMain.append(value1FI)
    orderMat.append(order1)
    for i in range(2,mo+1):
        combList=[]
        aveList=[]
        combList=list(combinations(order1,i))
        for j in range(0,len(combList)):
            summ=0
            for k in range(0,len(combList[j])):
                summ=summ+combList[j][k][1]
            ave=summ/len(combList[j])
            aveListPart=[]
            aveListPart.append(j)
            aveListPart.append(ave)
            aveList.append(aveListPart)
        aveList=sorted(aveList, key=lambda x: x[1],reverse=True)
        aveList=aveList[:x]
        valPart=[]
        for i in range(0,len(aveList)):
            valPart.append(aveList[i][1])
        valMain.append(valPart)    
        orderMatPart=[]
        FISetsPart=[]
        valSetsPart=[]
        for j in range(0,len(aveList)):
            indx=aveList[j][0]
            orderMatPart.append(combList[indx])
            FIPart=[]
            for k in range(0,len(combList[indx])):
                FIPart.append(combList[indx][k][0])
            FISetsPart.append(FIPart)
            valSetsPart.append(valPart)
        FIMain.append(FISetsPart)
        orderMat.append(orderMatPart)
    return FIMain,valMain
                
    
    
if __name__ == '__main__':
	main()