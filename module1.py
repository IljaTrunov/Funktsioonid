#def Pindala(külg1:float,külg2:float)->float:
 #   """Riistkülliku pindala leidmine 
#    :param float külg1:Riistikülliku esimene külg
#    :param float külg2:Riistikülliku teine külg
#    :rtype:float
#    """
#    S=külg1*külg2
 #   return S

 #Praktiline töö
 #1

def arithmetic(x:int,y:int,z:str):
	 """Saab teha +,-,*,/ ja tagastab arv, kui
	 vastus on on arv ja "Tundmatu tehe", kui ei saa vastust leida
	 :param float a: Esimene arv
	 :param float b: Teine arv
	 param str c: Aritmeetilise tehe
	 :rtype:var
	 """
	 #if z=="+":
		#B=x+y
		#return B
	 #elif z=="-":
		#B=x-y
		#return B
	# elif z=="*":
		#B=x*y
		#return B
	# elif z=="/":
		#B=x/y
		#return B
	 #else:
		 #pirnt("vale syntax")
#2
#def is_year_leap(a:int)->int:
	#"""
	#:param a: Aasta
	# """
	#if a%4==0:
		#return True
	#else:
		# return False
#3
#def square(a:float):
	# """
	#:param float a:
	# """
	#S=a**2
	#D=math.sqrt(2*S)
	#P=S**4
	#return S
	#return D
	#return P
#4
#def astaajad(m:int):
#    if m in (12,1,2):
#        return "talvel"
#    elif m in (3,4,5):
#        return "kevad"
#    elif m in (6,7,8):
#        return "suvi"
#    elif m in (9,10,11):
#        return "sügis"
# else:
#       m!=(1,2,3,4,5,6,7,8,9,10,11,12):
#                 print("Tundumatu kuu")

#5
#def bank(a:float, years:int):
	#"""
	#:parem float a: raha
	# :parem int years: aastad 
	# :
	#"""
	#D=years-2021
	#while D!=0:
		#D-=1
		#a=a/100*10+a
		#print(float(a))
		#return a
#6
#def is_prime(arv:int):
	#"""
	#:parem int a: number
	#"""
	#t=0
	#for i in range(1, arv+1):
		#if arv%i==0: t+=1
		#if t==2:
			#t=True
		#else:
			#t=False
	#return t
#7
#from datetime import *
#def date(day:int, month:int, year:int):
	#date(year,month,day)
