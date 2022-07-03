import os
import time
import base64


## please create two files newfile.txt1 and newfile.txt2
def base(file):
	f = open(file, "r").read().encode()
	fi = base64.b64encode(f)
	return fi
	
def merge(filelist):
	zi = open("newfile", "w")
	zi.write(f"newfile.txt1*&#{filelist[0].decode()}*&#")
	zi.write(f"newfile.txt2*&#{filelist[1].decode()}")

def unmerge(file):
	un = open(file, "r").read()
	un1 = un.split("*&#")
	
	r1 = open(un1[0], "w").write(base64.b64decode(un1[1].encode()).decode())
	
	r2 = open(un1[2], "w").write(base64.b64decode(un1[3].encode()).decode())
a = 1
while a == 1:
	new = [base("newfile.txt1"), base("newfile.txt2")] # comment to unzip
	merge(new) # comment to unzip
#	unmerge("newfile") #uncomment to unzip, please delete the two initial files and test it 
	a = a+1
	
	
