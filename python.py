#print the python
name="harshit yadav"
group="g1"
course="MCA"
print(name,group,course)

# type Casting  
# 2) find the age

salary = float("12345")
print(type(salary))
print(salary)

# 3) find the current age using input()

print("Enter your current year")
bornYear = int(input())
print("Enter your born year")
currentYear = int(input())
age = currentYear - bornYear
print(age)

# 4) Write a program of  currency converter
# convert dollar to rupees

print("Convert rupees to dollor")
rupeeAmount = int(input("Enter the amount in Rs."))
rsInToDollar = (rupeeAmount/84)
print(rupeeAmount, " convert into dollar", rsInToDollar)

#convert rupees to dollar

print("Convert dollar to rupees")
dollarAmount = int(input("Enter the amount in $."))
rsInToDollar = (dollarAmount*84)
print(dollarAmount, " convert into rupees", rsInToDollar)

# 5) write a program to check if you  are elidgible or not  for vote

userAge = int(input("Enter the age :"))
if userAge > 17 :
  print("You are eligible for vote")
else:
   print("You are not eligible for vote")


# 6) wap to check the user eligible for job app
# if gender is female and age is greater than 17
# if gender is male then they can apply for private job

userAge = int(input("Enter the age :"))
userGender = input("Enter the gender")
if(userAge >17 and userGender == "female"):
  print("You are eligible for job")
elif(userAge >17 and userGender == "male"):
 print("you are eligible for govt. job")
else:
 print("Your are not eligible for any job")


# 7) Write a program to find which one is greater among three number

a =int(input("Enter a first number"))
b = int(input("Enter a second number"))
c = int(input("Enter a third number"))
if(a>b and a>c):
    print(a, " - A is greater")
elif(b>a and b>c):
    print(b ," - B is greater")
else:
    print(c ," - C is greater")

# 8) Switch condition is replacement of multiple if else block

mytuple = ("Aman","pardeep", "Aytul","Adrash")
thistuple = ("shubhas", " shubham")

for x in mytuple:
  print(x)

# 9) use of dictonary in python

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#  10) if you want to print key  then 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# 11) use of  type 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# 12) use of oops in python

class harshit:
    age = 20
    print("i am form varanasi")
    harshit = harshit()
    print(harshit.age)

# 13 write a program  to print their age using class and object 

class AgeCalcu:
    currentYear = int(input("Enter your year"))
    lastYear = int(input("Enter your last year"))
    age = currentYear-lastYear
Age=AgeCalcu()
print(Age.age)






