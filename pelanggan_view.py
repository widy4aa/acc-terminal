import pelanggan_controller as controller
import helpers as helper
import dashboard_view as dashboard
from tabulate import tabulate

dump = [('Almashuda34', 'Huda', 'huda34678', 'owner')]


def menu_pelanggan_input():
    menu = int(input("pilih berdasarkan nomor :"))
    if 1 <= menu <=5 :
        return menu
    else : 
        menu_pelanggan_input()
        
def menu_pelangggan(status_login):
    #helper.dd(controller.select_data_pelanggan(controller.cur))
    print(tabulate(controller.select_data_pelanggan(controller.cur,),headers=['id_pelanggan','no_telp','nama_pelanggan','alamat'],))
    print (f"""---------------------------------------
           List Menu 
                    1.Tambah      3.Data Laptop       5.Kembali  
                    2.Edit        4.Data Transaksi    
            """)
    menu=menu_pelanggan_input()
    
    if menu == 1 :
        nama = input ("nama pelanggan : ")
        nomor_telp = input("nomor_telp : ")
        jalan = input("masukkan nama jalan : ")
        kecamatan = input("masukkan nama kecamatan : ")
        kabupaten = input("masukkan nama kabupaten : ")
        id_alamat = controller.cari_id_alamat(controller.cur)[0][0] + 1
        data_alamat = [id_alamat,jalan,kecamatan,kabupaten]
        data_pelanggan = [nama,nomor_telp,id_alamat]
        controller.input_data_alamat(controller.cur,data_alamat)
        controller.input_data_pelanggan(controller.cur,data_pelanggan)
        menu_pelangggan()
        
    elif menu == 2 :
        id_pelanggan = int(input("pilih id_pelanggan yang ingin di edit : "))
        data = controller.read_selection_table(controller.cur,'pelanggan','id_pelanggan',id_pelanggan )
        print(tabulate(data))
        print ("ganti value nya atau tidak dengan mengabaikan")
        nama_pelanggan = input((data[0][1]+' :')) or data[0][1]
        no_telp = input(data[0][2]+' :') or data[0][2]
        no_telp = input(data[0][3]+' :') or data[0][2]
    
        
    elif menu == 5 :
        helper.clear()
        dashboard.dashboard(status_login)
        
    
        
menu_pelangggan(dump)
