count = 0 #for counting the number of spaces
last_space = 0 #for remembering position of the last blabkspace  
inc = 0 #main word counter
x=0 # for couting position of word while printing
list1 = [] #storing all the lastspaces before 45th, 90th , 135th, and 180th character
#below is the text case which i made, cosnisting 4 , 5 or 6th characters only

abc = "Rajput into Octoer last year, recent share family image from here specia days tooo wish here fancy over New Years Howeve some follo wers gota dist ract with here ghoo nghat andy ques tioned here forom"
for i in abc:
	inc = inc+1
	if(i.isspace()) == True: 
		last_space= inc  #getting actual position of the last space
		count= count +1 
	if(inc ==45 and i.isalpha() == True):
		list1.append(last_space) #getting the immidiate last blank space through condition
	if(inc ==90 and i.isalpha() == True):
		list1.append(last_space) #and appending to the list.
	if(inc ==135 and i.isalpha() == True):
		list1.append(last_space)
	if(inc ==180 and i.isalpha() == True):
		list1.append(last_space)
	if(inc ==225 and i.isalpha() == True):
		list1.append(last_space)
	if(inc ==270 and i.isalpha() == True):
		list1.append(last_space)
		
print("space count",count)
print("total_space",last_space)
print("list",list1)
print("total words:",inc)
print("story is :")

for i in abc:
	x=x+1
	print(i, end="")
	if(x==list1[0]):
		print("\n")
	if(x==list1[1]):
		print("\n")
	if(x==list1[2]):
		print("\n")
	if(x==list1[3]):
		print("\n")
	if(x==200):
		print("\n")
	


