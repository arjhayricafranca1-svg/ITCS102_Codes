age = int(input("owner age   "))
revenue = float(input("what is you revenue   "))
cc = int(input("your credit score  "))
yrs = float(input("Yrs of bussiness  "))
has_default = bool(input("file for bankcrupcy    "))
c_name = input("collateral name   ")
c_val = float(input("collateral value    "))

max_loan = 0
base_fee = 0


if age >= 21 and has_default ==  False and yrs >= 2.0: #tier1
    print("baseline pass")
    if cc >= 720:
        print("credit score considerd high")
        max_loan = rev * 3
        #revenue
        if revenue >= 50000:
            print("mataas sa 50k")
            base_fee = max_loan *0.015
            print("base fee is set to", base_fee)
        else:
            print("mababa sa 50k")
            base_fee = max_loan *0.025
            print("base fee is set to", base_fee)

        #collateral
        if c_val >= max_loan:
            print("collateral"< c_name, "with a value of ", c_val, "is accepted")
        else:
            print("rejected: kulang collateral value mo", c_name)

        #surcharge
        if c_val % 5000 != 0:
            base_fee += 250
            print("additional charge added to base free, total base fee is", base_fee)
    elif cc <= 620 and cc < 720:#tier2
        print("creditscore mo ay range 620 to 720")
        if yrs >= 5.0:
            base_fee = max_loan * 0.02
            print("years mo sa business", base_fee)
        else:
            base_fee = max_loan * 0.035
        print("years mo sa business", base_fee)
    elif cc < 620:
        print("mababa cc mo")

    else:
        print("Invalid")
else:
    print("baseline failed ")