#inputs
sender_name = input("Enter sender name -----> ")
item_type = input("Enter type of item -----> ")
is_Fragile = input("Is the item is Fragile? (True or False) -----> ") == "True"
weight = float(input("Enter the weight(kg) -----> "))
distance = float(input("Enter the distance(km) -----> "))
is_Express = input("It is express? (True or False) -----> ") == "True" 
is_International = input("It is international? (True or False) -----> ") == "True"



#calculation Base cost
base_cost = (weight * 2.50) + (distance * 0.15)



#Evaluating pricing

if weight <= 2.0 and distance <=100 and not is_International:
	total = 0.00

elif is_International and is_Express:
	total = (base_cost * 1.40) + 50

elif is_Express or (is_International and weight >= 20):
	total = (base_cost * 1.20) + 25

elif weight >= 30 or distance >= 1000:
	total = base_cost + 30

else:
	total = base_cost


print("\n--- Shipping Summary ---")
print("Sender name:", sender_name)
print("Type of item:", item_type)
print("Fragile:", is_Fragile)
print("Weight:", weight)
print("Distance:", distance)
print("Express:", is_Express)
print("International:", is_International)
print("Total Shipping Charge: $ {:.2f}".format(total))