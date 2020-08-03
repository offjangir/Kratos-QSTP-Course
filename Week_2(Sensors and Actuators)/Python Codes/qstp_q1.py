#THIS PROGRAM CREATES A MATRIX OF THE POINTS AND RUNS TO GIVE THE POINTS WITH SMALLEST DISTANCE 
#PROVIDE THE POINTS AS STATED X1 Y1 Z1 X2 Y2 Z2 
import numpy as np
import math
print("The program will give shortest distant ponts pair in all points")
#--------------------------------------------------------------------------------------#
def matrix(R):
	print("Enter {} Elements(seperated by space** in format x1 y1 z1 x2 y2 z2.....and so on)" .format(R*3))
	a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:R*3] 
	b = np.asarray(a)
	x = b.reshape(R,3)
	return x

#--------------------------------------------------------------------------------------#	
while True:
	R = int(input("Enter number of points : "))
	if R>1:
		break
	else:
		print("Please Enter atleast 2 points")
x = matrix(R)
pre_i =0
pre_j =1
dis_n =0
i=0
while i <= R-1:
	j = i+1
	while j < R :
		dis = math.sqrt(np.sum(np.square(np.subtract(x[i],x[j]))))
		if i == 0 and j==1:
			dis_n = dis
		if dis_n > dis :
			dis_n = dis 
			pre_i = i
			pre_j = j
		j+=1
	i+=1
print("\nThe smallest distance is {} and the indices of points are {} {}.".format(dis_n,pre_i,pre_j))


#-------------------------------------------------------------------------------------------#















