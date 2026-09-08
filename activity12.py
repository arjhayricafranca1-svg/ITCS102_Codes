import getpass

username = 'wawawa1'
password = 'akosiako123'

u = input("Enter your username ----->")
p = getpass.getpass("Enter your password ----->")

if username == u and password == p :
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")