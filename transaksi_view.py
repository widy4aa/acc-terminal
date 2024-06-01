import helpers as helper 
import transaksi_controller as controller
from tabulate import tabulate

data_trx = controller.get_all_trx(helper.cur)
data_trx_now = controller.get_all_trx_now(helper.cur)
data_trx_month = controller.get_all_trx_month(helper.cur)


def detail_trx (data_detail,harga):
    print(f"""
Detail barang ----------------------
Data Transaksi Nya :

{tabulate(data_detail[0],headers=['id transaksi','nama pelanggan','pembuat','metode pembayaran','tanggal dibuat','keterangan'])}


product :

{tabulate(data_detail[1],headers=['id produk','nama produk','jenis produk','harga','kuantitas','total harga per produk'])}    

  
layanan :

{tabulate(data_detail[2],headers=['id layanan','nama layanan','harga','nama laptop'])}          
   
   
Total Bayar : {harga}
    """)   

def transaksi(status_login):
    if data_trx_now != []  :
        print("Data Transaksi Hari ini -----------------------")
        print(tabulate(data_trx_now,headers=['id transaksi','nama pelanggan','pembuat','metode pembayaran','tanggal dibuat','keterangan']))
    print (f"""---------------------------------------
         List Menu 
                  1.Tampilkan berdasar Bulan ini     3.Detail Trx
                  2.Tampilkan semua                  4.kembali   
          """)
    menu = helper.menu_input(4)
    
    if menu == 1 :
        print(tabulate(data_trx_month,headers=['id transaksi','nama pelanggan','pembuat','metode pembayaran','tanggal dibuat','keterangan']))
        input("enter untuk kembali :")
        helper.clear()
        transaksi(status_login)
    elif menu == 2 :
        print(tabulate(data_trx,headers=['id transaksi','nama pelanggan','pembuat','metode pembayaran','tanggal dibuat','keterangan']))
        input("enter untuk kembali :")
        helper.clear()
        transaksi(status_login)
    elif menu == 3 :
        id_transaksi = input("masukkan id transaksi ng ingin di cek : ")
        data_detail=controller.detail_trx(helper.cur,id_transaksi)
        harga = controller.total_bayar(helper.cur,id_transaksi)
        helper.clear()
        detail_trx(data_detail,harga)
        input("tekan enter untuk kembali ")
        helper.clear()
        transaksi(status_login)
    elif menu == 4 :
        helper.clear()
        transaksi(status_login)
    
