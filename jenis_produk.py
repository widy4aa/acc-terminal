import helpers as helper
import jenis_produk_controller as controller
import produk_view as produk
from tabulate import tabulate


def menu_jenis(status_login):
    print("--------------------------")
    data_jenis=controller.get_all_jenis(controller.cur)
    print(tabulate(data_jenis,headers=['id_jenis_produk','jenis_produk']))
    print (f"""---------------------------------------
           List Menu 
                    1.Tambah      3.Hapus      
                    2.Edit        4.Kembali   
            """)
    menu=helper.menu_input(4)
    
    if menu == 1 :
        jenis = input("masukkan jenis produk : ")
        controller.add_jenis(controller.cur,jenis)
        helper.clear()
        menu_jenis(status_login)
        
    elif menu == 2:
        id_jenis = input('pilih id yang ingin di edit : ')
        jenis = controller.get_select_jenis(controller.cur,id_jenis)
        jenis_baru = input((jenis[0][1] + " : ")) or jenis[0][1]
        helper.clear()
        controller.update_jenis(controller.cur,id_jenis,jenis_baru)
        menu_jenis(status_login)
        
    elif menu == 3 :
        id_jenis = input('pilih id yang ingin di hapus : ')
        controller.delete_jenis(controller.cur,id_jenis)
        helper.clear()
        menu_jenis(status_login)
        
    elif menu == 4 :
        helper.clear()
        produk.menu_produk(status_login)

       

    