#PESO DENOMINATIOR
# MONEY 4572
# 1000, 500, 200, 100, 50, 20, 10, 5, 1 

#what operator / symbol did you use to solve the problem 
# floor division, % modulus 


money = 4572
libo = money // 1000 #4.6 --> 4
libo_sukli = money % 1000 #572
#libo_sukli = money - (libo * 1000)

five_h = libo_sukli // 500 
five_sukli = libo_sukli % 500 # 72


two_h = five_sukli // 200
two_sukli = five_sukli % 200

hundred = two_sukli // 100
sukli_h = two_sukli % 200

fifty = sukli_h // 50
fifty_sukli = sukli_h % 50

bente = fifty_sukli // 20
bente_sukli = fifty_sukli % 20

sampo = bente_sukli // 10
sampo_sukli = bente_sukli % 10

payb = sampo_sukli // 5
payb_sukli = sampo_sukli % 5


piso = payb_sukli // 1
siro = payb_sukli % 1



print ("1000 - ", libo)
print ("500 -", five_h)
print ("200 -", two_h)
print ("100 -", hundred)
print ("50 -", fifty)
print ("20 -", bente)
print ("10 -", sampo)
print ("5 -", payb)
print ("1 -", piso)



