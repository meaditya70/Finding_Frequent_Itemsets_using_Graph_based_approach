f = open("data/mushroom.txt","r")
d = f.readlines()
	
inputList=[x.split() for x in d]
nameList=[]
	
n=len(inputList[0][0])
iter=(n+1)/2
	
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

print(nameList)

print("Enter Index: ")
indx=input()
indx=int(indx)

count=0
for i in range(0,len(nameList)):
	for j in range(0,len(nameList[i])):
		if(count==indx):
			print("i,j=",i+1,j+1)
			print("nameList[i]=", nameList[i])
			print("nameList[i][j]=",nameList[i][j])
		count=count+1