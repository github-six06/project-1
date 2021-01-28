question="please input a number,"
question+="and I will tell you if this number can be divisible by 10."
number=input(question)
number=int(number)
if number%10==0:
	print("Yes,it can be")
else:
	print ("No,it can't be")
