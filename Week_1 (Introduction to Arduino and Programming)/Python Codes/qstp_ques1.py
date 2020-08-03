#PROGRAM TO FIND PRIME NUMBERS IN THE INPUT LIST#


import math
print("WELCOME PLEASE INPUT 10 NUMBERS TO FIND PRIMES AMONG THEM")
num =[] #input array/list
prime =[]
a=0
while a>=0 :
    t=int(input("Enter Number:"))
    if t>0:#FOR CHECKING VALID POSITVE ENTRIES IN THE INPUT LIST
    	num.append(t)
    	a+=1
    	if a==10:
    		break#FOR LIMITING THE INPUT ENTRIES IN LIST TO 10
    else:
    	print("Enter a Positive Number")
    

#resetting value of a to use again
i=0#initializing i
#initializing n
while i<10:
	a=num[i]
	m = 0 
	if a>2:
		n=2
		while n <= math.sqrt(a):#THERE WILL BE PRIME IF NO FACTORS ARE FOUND BEFOR ROOT OF NUMBER
			if a%n == 0:
				m+=1
			n+=1
	if m == 0:
		if a >=2:
			prime.append(a)#ADDING NUMBER TO THE LIST
	i +=1
#PRINTING THE LIST OF PRIME NUMBERS
for i in range(len(prime)):
	print prime[i]






