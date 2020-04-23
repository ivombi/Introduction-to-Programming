#Writing a file
myfile = open("test.csv","w")
myfile.write("My first file written from python\n")
myfile.write("....................................\n")
myfile.write("Hello, world!\n")
myfile.close()

#Reading a file
mynewhandle = open("test.txt","r")
while True:
    theline = mynewhandle.readline()
    if len(theline)==0:
        break
    print(theline,end="")