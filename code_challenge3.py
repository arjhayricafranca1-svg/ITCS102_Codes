name = input("Sender_Name ----> ")
name1 = input("Type_of_item  ----> ")
isFragile = bool(input("Is that Fragile ? ----> ")) 

if isFragile == True and isFragile == False:
	print("Fragile")
else:
	print("not_Fragile")


weight = float(input("Weight of the item ? ----> "))


if weight >= 1.5kg and weight <= 9.9kg:
	print("$0.00")
else:
	print("0.00")