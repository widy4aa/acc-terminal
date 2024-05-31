import helpers as helper
import jenis_produk as jp
import dashboard_view as dashboard
import jenis_produk_controller as jpcontroller
import produk_controller as controller
from tabulate import tabulate


def menu_produk (status_login):
    print("----------------------------")
    data_produk = controller.get_all_produk(controller.cur)
    print(tabulate(data_produk,headers=['id_produk','nama_produk','harga','jenis']))
    print (f"""---------------------------------------
         List Menu 
                  1.Tambah Produk     3.Jenis Produk
                  2.Edit Produk       4.kembali   
          """)
    menu = helper.menu_input(4)
    
    if menu == 1 :
        data_jenis = jpcontroller.get_all_jenis(helper.cur)
        nama_produk = input("masukkan nama produk : ")
        harga_produk = input("masukkan harga : ")
        print(tabulate(data_jenis,headers=['id_jenis','jenis_produk']))
        id_jenis_produk = input("masukkan id jenis produk berdasarkan data di atas : ")
        controller.add_produk(helper.cur,[nama_produk,harga_produk,id_jenis_produk])
        helper.clear()
        menu_produk(status_login)
    
    elif menu == 2 :
        id_produk = input("masukkan id produk yang ingin di edit : ")
        data_produk = controller.select_product(helper.cur,id_produk)
        nama_produk = input((data_produk[0][1] + " :")) or data_produk[0][1]
        harga_produk = input((str(data_produk[0][2]) + " :")) or data_produk[0][2]
        data_jenis = jpcontroller.get_all_jenis(helper.cur)
        print(tabulate(data_jenis,headers=['id_jenis','jenis_produk']))
        id_jenis_produk = input("masukkan id jenis produk berdasarkan data di atas : ")
        controller.edit_produk(helper.cur,id_produk,[nama_produk,harga_produk,id_jenis_produk])
        helper.clear()
        menu_produk(status_login)
        
    elif menu == 3 :
        helper.clear()
        jp.menu_jenis(status_login)
        
    elif menu == 4 :
        helper.clear()
        dashboard.dashboard(status_login)
        
    
