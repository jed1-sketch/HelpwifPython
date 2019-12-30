myfile=open("name.txt","r+")
list1=["test1","test2","test3","test4"]
myfile.writelines(list1)

print (myfile.readlines())
myfile.close()
