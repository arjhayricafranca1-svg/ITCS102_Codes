money = eval(input("Enter amount to deposit: "))

#denominations
c1000 = 1000
c500 = 500
c200 = 200
c100 = 100
c50 = 50
c20 = 20
c10 = 10
c5 = 5
c1 = 1 

#calculations 
thousands = money//c1000
money%= c1000
five_hundreds = money//c500
money%= c500
two_hundreds = money//c200
money%= c200
hundreds = money//c100
money%= c100
fifties = money//c50
money%= c50
twenties = money//c20
money%= c20
tens = money//c10
money%= c10
fives = money//c5
money%= c5
ones = money//c1
money%= c1

#output
print("\nHEre is a breakdown, using PH demonstration:")
print("1000:", thousands)
print("500:", five_hundreds)
print("200:", two_hundreds)
print("100:", hundreds)
print("50:", fifties)
print("20:", twenties)
print("10:", tens)
print("5:", fives)
print("1:", ones)

