#While loop 

mahal = True #booleam to 
while mahal == True:
    x = bool(input("Mahal naba ang gas o bigas?? (True/False) "))
    if x == True:
        print("bigas?")
        continue
    else:
        print("ikaw di mahal")
        break