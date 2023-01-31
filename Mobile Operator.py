import math
tel=str(input("Enter your mobile number in 11 digits (eg 09123456789): "))
if len(tel)!=11 or tel[0:2]!="09":
 print("You entered the wrong number")
 exit()
if tel[0:3]=="091": 
 print("Your operator is HamraheAval") 
elif  tel[0:3]=="093":
 print("Your operator is Irancell") 
elif  tel[0:3]=="095":
  print("Your operator is Ritell")  
else:
  print("Your number is not valid in Iran")  
   