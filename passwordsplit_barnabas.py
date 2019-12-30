fileData=[]
fileData=["'Kofi,chicken'='Ama,cat'='kwame,frog'"]

oldData=fileData.split("=")
print (oldData[0])

for x in oldData:
    newData=oldData.split(",")
    for q in newData:
	    euSername=newData[0]
	    uSerpassword=newData[1]

print (uSerpassword)
print (uSername)