###THIS PROGRAM HAS BEEN MADE AS THE INSTRUCTIONS GIVEN IN THE QSTP PAPER WEEK_1
import time

### REFER README.MD FOR DETAILS

class Coder:##THE CLASS
	def __init__(self,name,age,lang,pro,xp):
		self.name =name
		self.age=age
		self.lang=lang
		self.pro=pro
		self.xp=xp


	def info(self):#METHOD TO GIVE INFO
		print("Hello World! My name is {}.I am aged {}.I have a experience level of {}." .format(self.name,self.age,self.xp))
		if len(self.lang) == 0 :
			print("\nHe knows no languaegs.")
		else :
			print("Language(s) known are",','.join(self.lang) ,end='.')
		if len(self.pro) == 0 :
			print("He has done no projects.")
		else :
			print("Project(s) I have done is/are", ','.join(self.pro) ,end='.')
	def addlang(self,language):##METHOD TO ADD LANGUAGE
		self.lang.append(language)
		
		self.xp = self.xp + 10
	def addproj(self,project):##METHOD TO ADD PROJECTS
		self.pro.append(project)
		
		self.xp = 1.5*self.xp



#c1 = Coder("yash",20,['python','cpp'],['kratos'],0)
#c1.info();
## this is just a demo instance added in comments

print("\nWelcome to the Coder Information\n")##Intro to the program

####################----------------START OF CONTROL PROGRAM THIS LOOP WILL RUN AND ADD INFO--------------##############


while True :#INFINITE LOOP WILL DRIVE PROGRAM TILL USER WISHES THE EXIT
	print("Please select one of  by typing the serial no.:- \n 1.Add new coder \n 2.exit")
	a = int(input("Enter Serial no."))#USER NEEDS TO ENTER A INPUT TO START ADDING CODER
	if a>2:
		print("Invalid Option")
	elif a<1:
		print("Invalid Option")
	elif a == 1 :
		#try:     ##tTHIS CAN BE USED FOR EXCEPTI0N HANDLING IF THE  ADMIN WISHES TO DO SO
		print("Adding Coders")
		name = input("Enter Name of Coder:-\t")
		age = int(input("Enter age of Coder:-\t"))
		i = int(input("Enter no. of languages known:-\t"))
		n=0
		while n<i:##ADDING LANGUAGES IN CLASS
			l = input("Enter language:-\t")
			la= []
			la.append(l)
			n+=1
		i = int(input("Enter no. projects:-\t"))
		n=0
		while n<i:#ADDING PROJECTS IN CLASS
			p = input("Enter project:-\t")
			pr=[]
			pr.append(p)
			n+=1
		xp = int(input("Enter xp:-\t"))
		k = Coder(name,age,la,pr,xp)
		print("Coder added")
		#except:
			#print("Wrong Input")
			#break

		print("\nType L if you want to add new language for this coder OR Type Press E for exit OR Press any for moving further.\t")
		alpha = input("")#A GOOD USER INTERFACE WILL ASK WHAT USER WANTS TO DO AND PERFROM ACTIONS
		if alpha == 'L':
			print("Adding new Language......!!\n")
			while True :
				lang = input("Enter Language to add or press E to end addtion of language(s).\t")
				if lang == 'E':
					break
				else:
					k.addlang(lang)#USING METHOD CRETED IN CLASS TO ADD LANG
					print("Language(s) added.")
		if alpha == 'E':
			print("Exiting")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			exit()
		print("\nType P if you want to add new Project for this coder OR Type Press E for exit.OR Press any for moving further.\t")
		alpha = input("")#A GOOD USER INTERFACE WILL ASK WHAT USER WANTS TO DO AND PERFROM ACTIONS
		if alpha == 'P':
			print("Adding new Project.....!!\n")
			while True :
				pro = input("Enter Language to add or press E to end addtion of Project(s).\t")
				if pro == 'E':
					break
				else:
					k.addproj(pro)#USING METHOD CRETED IN CLASS TO ADD PROJECT
					print("Project(s) added.")
		if alpha == 'E':
			print("Exiting")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			exit()
		alpha = input("Do You want a final info on this coder (Y/N) ? \t")
		if alpha == 'Y':
			k.info()#A FINAL INFOR CAN BE EXTRACTED BY PRESSING Y
		alpha = input("Do You want to add more coders (Y/N)?\t")
		if alpha == 'Y':
			continue
		else: 
			print("Exiting")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			exit()
#KEEP ON ADDING CODERS UNTIL USER WISHES TO EXIT
	else:
		print("Exiting")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		exit()#PROVIDES AND EXIT AT ANY STAGE OF THE PROGRAM
##################----------------------- END CONTROL PROGRAM -----------------------############################