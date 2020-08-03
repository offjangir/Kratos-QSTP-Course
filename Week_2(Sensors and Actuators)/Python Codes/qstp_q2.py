#THE PROGRAMS ASKS FOR THE INFECTED HOUSES CORDINATES AND THENGIVES BACK THE HOUSES THAT ARE PRONE TO INFECTION BY A SIMPLE ALORITHM
#PROVIDE INPUTS AS ASKED AND WATCH OUT FOR THE  COORDINATES TO BE FROM 0-9 0-9
import numpy as np
#--------------------------------------------------------------------------------------------------------------------#
def matrix():
	print("YOU NEED TO PROVDE THE MATRIX COORDINATES OF HOUSES WHICH ARE INFECTED")
	t = np.zeros(shape = (10,10))
	while True:
		alpha = int(input("ENTER 1 TO ADD INFECTED AND ANY TO CALCULATED TOTAL INFECTED(CONSIDER COORDINATES FROM 0-9 AND 0-9) : "))
		
		if alpha == 1:
			i = int(input("GIVE X COORDINATE : "))
			j = int(input("GIVE Y COORDINATE : "))
			if (i>9 or j>9) and (i<0 or j<0):
				print("WRONG INPUT")
			else: 
				t[j][i] = 1
		else: break
	return t
#------------------------------------------------------------------------------------------------------------------#
def Check_covid(t):
	house =0
	for i in range(p):
		for j in range(p):
			if (i > 0 and i < p-1) and (j>0 and j< p-1):
				if t[i][j] == 1 or t[i-1][j-1] == 1 or t[i-1][j] == 1 or t[i-1][j+1] == 1 or t[i][j-1] == 1 or t[i][j+1] == 1 or t[i+1][j-1] == 1 or t[i+1][j] == 1 or t[i+1][j+1] == 1:
					house+=1
					
			elif i ==0  and j ==0:
				if t[0][j+1]==1 or  t[i+1][j+1]==1 or t[i+1][j] ==1 or t[i][j]==1:
					house+=1
					
			elif i == p-1  and j ==0:
				if t[i][j]==1 or  t[i-1][j+1]==1 or t[i-1][j]==1 or t[i][j+1]==1:
					house+=1
					
			elif i ==0  and j ==9:
				if t[i][j]==1 or  t[i][j-1]==1 or t[i+1][j-1]==1 or t[i+1][j]==1:
					house+=1
					
			elif i ==0  and j ==9:
				if t[i][j]==1 or  t[i][j-1]==1 or t[i+1][j-1]==1 or t[i+1][j]==1:
					house+=1
					
			elif i ==9  and j ==9:
				if t[i][j]==1 or  t[i-1][j]==1 or t[i-1][j-1]==1 or t[i][j-1]==1:
					house+=1
					
			elif i == 0 and (j>0 and j <9) :
				if t[i][j]==1 or  t[i+1][j-1]==1 or t[i+1][j]==1 or t[i+1][j+1]==1 or t[i][j-1]==1 or t[i][j+1]==1:
					house+=1
					
			elif i == 9 and (j>0 and j <9) :
				if t[i][j]==1 or  t[i-1][j-1]==1 or t[i-1][j]==1 or t[i-1][j+1]==1 or t[i][j-1]==1 or t[i][j+1]==1:
					house+=1
					
			elif j == 0 and (i>0 and i-1 <9) :
				if t[i][j]==1 or  t[i-1][j+1]==1 or t[i][j+1]==1 or t[i+1][j+1]==1 or t[i-1][j]==1 or t[i+1][j]==1:
					house+=1
					
			elif j == 9 and (i>0 and i <9) :
				if t[i][j]==1 or  t[i-1][j-1]==1 or t[i-1][j]==1 or t[i][j-1]==1 or t[i+1][j-1]==1 or t[i+1][j]==1:
					house+=1
					
			else:
				pass
	print(house)
	return 
#-----------------------------------------------------------------------------------------------------------------------#
p = 10
t = matrix()
print(t)
Check_covid(t)

#------------------------------------------------------------------------------------------------------------------------#



 