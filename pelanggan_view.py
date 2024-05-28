import pelanggan_controller as controller
import helpers as helper
import dashboard_view as dashboard
import pc_view as pc
from tabulate import tabulate

#dump = [('Almashuda34', 'Huda', 'huda34678', 'owner')]


def menu_pelanggan_input():
    menu = int(input("pilih berdasarkan nomor :"))
    if 1 <= menu <=4 :
        return menu
    else : 
        menu_pelanggan_input()
        
def menu_pelangggan(status_login):
    #helper.dd(controller.select_data_pelanggan(controller.cur))
    print(tabulate(controller.select_data_pelanggan(controller.cur,),headers=['id_pelanggan','nama_pelanggan','no_telp','alamat'],))
    print (f"""---------------------------------------
           List Menu 
                    1.Tambah      3.Data Laptop      
                    2.Edit        4.Kembali    
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
        menu_pelangggan(status_login)
        
    elif menu == 2 :
        id_pelanggan = int(input("pilih id_pelanggan yang ingin di edit : "))
        data = controller.read_pelanggan_selection(controller.cur,id_pelanggan )
        print(tabulate(data))
        print ("ganti value nya atau tidak dengan mengabaikan")
        data_pelanggan = helper.read_selection(controller.cur,id_pelanggan,'id_pelanggan','pelanggan')
        data_alamat = helper.read_selection(controller.cur,id_pelanggan,'id_alamat','alamat')
        nama_pelanggan = input((data_pelanggan[0][1] + " :") ) or data_pelanggan[0][1]
        no_telp = input((data_pelanggan[0][2] + " :") ) or data_pelanggan[0][2]
        jalan = input((data_alamat[0][1] + " :") ) or data_alamat[0][1]
        kecamatan = input((data_alamat[0][2] + " :") ) or data_alamat[0][2]
        kabupaten = input((data_alamat[0][3] + " :") ) or data_alamat[0][3]
        data_pelanggan_baru = [id_pelanggan,nama_pelanggan,no_telp,id_pelanggan]
        data_alamat_baru  = [id_pelanggan,jalan,kecamatan,kabupaten]
        controller.update_pelanggan(controller.cur,id_pelanggan,data_pelanggan_baru)
        controller.update_alamat(controller.cur,id_pelanggan,data_alamat_baru)
        menu_pelangggan(status_login)
        
    elif menu == 3 :
        helper.clear()
        pc.menu_pc(status_login)
        
        
    elif menu == 4 :
        helper.clear()
        dashboard.dashboard(status_login)
        
    
        
#menu_pelangggan(dump)
