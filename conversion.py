from itertools import combinations
import csv

def combo(list1):
	comb=[]
	comb=list(combinations(list1, 2))
	return comb

#reading File
def convertToMBD(file_name):
    f = open(file_name,"r")
    d = f.readlines()
    inputList=[x.split() for x in d]
    
    #creating the nameList
    nameList=[]
    n=len(inputList[0][0])
    iter=int((n+1)/2)
    loop=0
    q=0
    while(loop<iter):
    	nameListPart=[]
    	for loop1 in range(0,len(inputList)):
    		nameListPart.append(inputList[loop1][0][q])
    	myset=set(nameListPart)
    	nameListPart=list(myset)
    	nameListPart=sorted(nameListPart)
    	nameList.append(nameListPart)
    	q=q+2
    	loop=loop+1
    
    #conversion to MBD
    finallist=[]
    i=0
    while(i<len(inputList)):   
    	finallistPart=[]
    	q=0
    	for j in range(0,iter):
    		list1=[0]*len(nameList[j])
    		for k in range(0,len(nameList[j])):			
    			if(inputList[i][0][q]==nameList[j][k]):
    				list1[k]=1
    		q=q+2
    		finallistPart.append(list1)
    	finallist.append(finallistPart)
    	i=i+1	
    print(finallist[0][0])
    convertedList=[]
    for i in range(0,len(finallist)):
    	convertedListPart=[]
    	for j in range(0,len(finallist[i])):
    		convertedListPart=convertedListPart+finallist[i][j]
    	convertedList.append(convertedListPart)
    
    with open("data/mbd.txt",'w') as f:
    	writer = csv.writer(f)
    	writer.writerows(convertedList)
    	
    print("nameList =",nameList)
    print("len(finalList) =",len(finallist))
    print("finalList[0] =",finallist[0])
    print("len(convertedList) =",len(convertedList))
    print("convertedList[0] =",convertedList[0])
    return convertedList,nameList

def convertToWeights(inputList,nameList):
    indices=[]
    db=[]
    loop=0
    while (loop<len(inputList)):
        indices = [i for i, x in enumerate(inputList[loop]) if x == 1]
        db.append(indices)
        loop=loop+1

    loop=0
    combList=[]
    while (loop<len(db)):
        cl=[]
        cl=combo(db[loop])
        combList=combList+cl
        loop=loop+1

    abc=0
    ba=[]
    database=[]
    while abc<len(inputList[abc]):
        ba=[0]*len(inputList[abc])
        database.append(ba)
        abc=abc+1
    loop=0
    while loop<len(combList):
        i1=combList[loop][0]
        i2=combList[loop][1]
        database[i1][i2]=database[i1][i2]+1
        database[i2][i1]=database[i2][i1]+1
        loop=loop+1
	
	
    with open("data/newdatabase.txt",'w') as f:
        writer = csv.writer(f)
        writer.writerows(database)
    
    print("len(database) =",len(database))
    print("len(database[0]) =",len(database[0]))

def main():
    file_name="data/kr-vs-kp.data.txt"
    inputList=[]
    nameList=[]
    inputList,nameList=convertToMBD(file_name)
    convertToWeights(inputList,nameList)

    

if __name__ == '__main__':
    main()