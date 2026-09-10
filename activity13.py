name = input("Input your NAME -----> ")
age = int(input("Input your AGE -----> "))


#rint("Hi," ,name, " that age consider as ")
if age >= 1 and age <= 5:
	print("infant")

elif age >= 6 and age <= 12:
	print("Kid")

elif age >= 13 and age <= 19:
	print("teenager")

elif age >= 20 and age <= 29:
	print("early adult")

elif age >= 30 and age <= 48:
	print("adult")


else:
	print("Invalid!")