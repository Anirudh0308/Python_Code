with open("this.txt", "r") as f:
    content1 = f.read()

with open("this_copy.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("this file are identical")
else:
    print("no, this file are not identical")
