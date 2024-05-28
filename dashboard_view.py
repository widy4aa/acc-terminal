import datetime
import pelanggan_view as pelanggan
import dashboard_controller as controller
import helpers as helper
import profile_view as profile
import pengguna_view as pengguna
from tabulate import tabulate

#dump = [('Almashuda34', 'Huda', 'huda34678', 'owner')]

#dashboard

def searching_dashboard (status_login): 
    inputan = input("cari :")
    data_pelanggan=controller.searching_pelanggan(controller.cur,inputan)
    data_produk=controller.searching_produk(controller.cur,inputan)
    data_layanan=helper.searching(controller.cur,inputan,"layanan","nama_layanan")
    print("\n")
    print("dari pelanggan")
    print(tabulate(data_pelanggan,headers=['id_pelanggan','nama_pelanggan','alamat']))
    print("\n")
    print("dari layanan")
    print(tabulate(data_layanan,headers=['id_layanan','nama_layanan','harga']))
    print("\n")
    print("dari produk")
    print(tabulate(data_produk,headers=['id_layanan','nama_produk','harga','jenis']))
    jeda = input("tekan enter untuk kembali")
    helper.clear()
    dashboard(status_login)

def dashboard (status_login):
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
    1.Searching      3.Pemesanan         5.Data Produk      7.Data Pengguna
    2.Data Pelanggan 4.Data Transaksi    6.Data Layanan     8.Profile        
           """)
    inputan = controller.menu_dashboard_input()
    helper.clear()

    if inputan == 1 :
        helper.clear()
        searching_dashboard(status_login)
       
        
    elif inputan == 2 :
        helper.clear()
        pelanggan.menu_pelangggan(status_login)
        
    
    elif inputan == 7 and status_login[0][3] == 'owner' :
        helper.clear()
        pengguna.pengguna(status_login)

    elif inputan == 8:
        helper.clear()
        profile.menu_profile(status_login)
    
    else: 
        dashboard(status_login)

        
      
#dashboard(dump)