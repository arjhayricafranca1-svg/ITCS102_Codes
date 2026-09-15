# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int(input("Enter your age    > "))
is_employed = bool(input("Are you currently employed > ")) 
credit_score = int(input("Credit score   > "))
annual_income = float(input("What is your annual salary   > "))
has_collateral = bool(input("Do you have collateral (True/False) > ")) == "true"

base_rate = 0.0

if age >= 21 and is_employed:
    print("Accepted base line Criteria")
    if credit_score >= 750  and has_collateral:
         print("you have high credit score")
         if annual_income >= 100000:
            base_rate = 4.5
            print("Your base rate is ", base_rate,  ) 
        else:
            base_rate = 5.0
            print("Your base rate is ", base_rate)
    elif credit_score >= 600 and   credit_score < 750:
            print("Your credit score is less than 750")
        if has_collateral == True:
            print("you have collateral ")
            base_rate = 7.0
            print("your base rate is", base_rate)
        elif annual_income <= 40000:
            print("Low annual income")
            base_rate = 9.5
            print("Your base interest is", base_rate)
        else:
           base_rate = 8.0 
          print("Your base rate is ", base_rate)
        if credit_score < 600:
            print("Your credit score is less than 600")
            base_rate = 10.0
            print("Your base rate is ", base_rate)
        else:
            print("Your credit score is less than 600")
            base_rate = 10.0
            print("Your base rate is ", base_rate)
else:
    print("Rejected Fails baseline criteria")
