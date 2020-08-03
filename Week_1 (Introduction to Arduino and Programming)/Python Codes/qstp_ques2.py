#PROGRAM  FOR A SIMPLE CALCULATOR IN PYTHON 
import time
import math

print("Calculator")#HEADING
while True:
	oper = raw_input("Choose a math operation (+, -, *,/): or Type E for Exit!!\t")
	if oper == 'E': #EXIT
		print("Exiting")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		exit()
	a = float(input("Enter the first number:"))
	b = float(input("Enter the second number:"))
	if oper == '/':#DIVIDE WITH EXCEPTION HANDLING
		try:
			c = (a/b)
			print 'The answer is',c 
		except:
			print('Divisor cannot be 0.ANSWER will become not defined.')
	elif oper == '*':#MULTIPLICATION
		c = (a*b)
		print 'The answer is',c 
	elif oper == '-':#SUBTRACTION
		c = (a-b)
		print 'The answer is',c 
	elif oper == '+':#ADDITION
		c = (a+b)
		print 'The answer is',c 
	else:
		print("Please select a valid option.")



