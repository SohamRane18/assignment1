# file
def fileFunction(file="file1.txt"):
    try:
        File=open(file,"a+t")
        File.writelines(["Roll No:18\n","Name: Soham Rane\n"])
        File.seek(0)
        print(File.readlines())
    except Exception as e:
        print(e)

# File Function
def fileFunction(file="File1.txt"):
    try:
        File=open(file,"a+t")
        File.writelines(["Roll No:18\n","Name: Soham Rane\n","Class: SYCO-A\n"])
        File.seek(0)
        print(File.readlines())
    except Exception as e:
        print(e)

fileFunction()