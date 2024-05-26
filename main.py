import configparser
import pandas
import tabulate
import datetime
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
print (f"sekarang tanggal {datetime.date.today()}")
print (f"selamat datang {status} {nama}")
transaksi_hari_ini = controller.read_jumlah_data(controller.cur,"transaksi")
print (f"jumlah transaksi hari ini : {transaksi_hari_ini[0][0]}")
print (f"jumlah uang masuk hari ini : {controller.read_jumlah_uang_masuk(controller.cur)}")
print (f"produk dan atau layanan yang paling diminati hari ini : {controller.produk_layanan_diminati(controller.cur)}")
pembayaran_hari_ini = controller.metode_pembayaran_diminati(controller.cur)
print (f"jenis pembayaran paling diminati : {pembayaran_hari_ini[0][0]} ")
print("-------------------------------")

#menu

print (f"""List Menu 
1.Searching      3.Pemesanan         5.Data Produk       7.Data Layanan
2.Data Pelanggan 4.Data Transaksi    6.Data Pengguna     8.Profile        
       """)

menu = int(input("pilih berdasarkan nomor :"))