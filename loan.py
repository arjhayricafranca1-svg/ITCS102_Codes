loan_amount = float(input("Enter the loan ? "))
year = int(input("Enter year to pay? "))
month = year * 12 
principal = loan_amount / month
remain_bal = loan_amount
total = 0
#loan_int = pass
#monthly_pay = pass



print("|MONTH\t|\tPAYMENT\t\t|\tINTEREST\t|\tPRINCIPAL\t|\tBALANCE\t\t|")
for x in range(1, month + 1):
    remain_bal -= principal
    loan_int = remain_bal * 0.00256
    monthly_pay = loan_int + principal
    #print(x ,(monthly_pay, 2), loan_int, round( principal, 2 ) , round(remain_bal, 2))
    print(f"|{x}\t|\t{round(monthly_pay, 2)}\t\t|\t{round(loan_int,2)}\t\t|\t{round( principal, 2)}\t\t|\t{round(remain_bal, 2)}\t\t|")
    #print(f"1{x} \t | {round(monthly_pay)} \t | \t {round(loan_int)} \t | \t {round(principal)} \t | \t {round(remain_bal)}")