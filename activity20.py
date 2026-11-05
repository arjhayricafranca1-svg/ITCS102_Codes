from getpass import getpass

isLogin =  False

while isLogin == False:
    username = input("Username: ----> ")
    password = getpass("Password: ---->")

    if username == "akoangbagyo1" and password == "akobato1":
        print("access granted")
        isLogin = True
    else:
        print("Incorrect")