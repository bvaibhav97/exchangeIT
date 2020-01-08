f= open("guru99.txt","w+")
f.write("hiii this is vaibhav")
f.close()

f= open("guru99.txt","r")
contents = f.read()
for i in contents:
	if i == "\n":
		print("found")
	print(i , end=' ')