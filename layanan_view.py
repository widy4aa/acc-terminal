import helpers as helper
import layanan_controller as controller
import dashboard_view as dashboard
from tabulate import tabulate

def menu_layanan(status_login):
    print("--------------------------------------------")
    data_layanan = controller.get_all_layanan(helper.cur)
    print(tabulate(data_layanan,headers=['id_layanan','nama layanan','harga']))
    print (f"""---------------------------------------
         List Menu 
                  1.Tambah Layanan     3.Hapus Layanan      
                  2.Edit Layanan       4.kembali   
          """)
    menu = helper.menu_input(4)
    if menu == 1 :
        nama_layanan=input("masukkan nama layanan : ")
        harga = input("masukkan harga : ")
        controller.tambah_layanan(helper.cur,[nama_layanan,harga])
        helper.clear()
        menu_layanan(status_login)
    elif menu == 2 :
        id_layanan = input("masukkan id layanan : ")
        data_lama = controller.get_selection_layanan(controller.cur,id_layanan)
        nama_layanan = input((data_lama[0][1] + " :")) or data_lama[0][1]
        harga = input((str(data_lama[0][2]) + " :")) or data_lama[0][2]
        controller.edit_layanan(helper.cur,[nama_layanan,harga],id_layanan)
        helper.clear()
        menu_layanan(status_login)
    elif menu == 3 :
        id_layanan = input("masukkan id layanan yang ingin dihapus : ")
        controller.delete_layanan(helper.cur,id_layanan)
        helper.clear()
        menu_layanan(status_login)
    elif menu == 4 :
        helper.clear()
        dashboard.dashboard(status_login)

