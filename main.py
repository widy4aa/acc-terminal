import configparser
import pandas
import tabulate
import controller as controller

#login 

print("░█████╗░░█████╗░░█████╗░")
print("██╔══██╗██╔══██╗██╔══██╗")
print("███████║██║░░╚═╝██║░░╚═╝")
print("██╔══██║██║░░██╗██║░░██╗")
print("██║░░██║╚█████╔╝╚█████╔╝")
print("╚═╝░░╚═╝░╚════╝░░╚════╝░")
print("Jual Beli dan service Computer")
print("-------------------------------")
while True:
    print("Login Masukkan username dan password yang benar")
    username=input("username :")
    password=input('password :')
    status_login = controller.login(username,password)
    if status_login:
        print('berhasil login')
        break
    

#dashboard