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
    username=input("username :") or 'Almashuda34'
    password=input('password :') or 'huda34678'
    status_login = controller.login(username,password)
    if status_login:
        print('berhasil login')
        break
    

#dashboard
print("-------------------------------")
nama = status_login[0][1]
status = status_login[0][3]
print (f"selamat datang {status} {nama}")