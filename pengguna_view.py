import pengguna_controller as controller
import dashboard_view as dashboard
import helpers as helper
from tabulate import tabulate



def pengguna(status_login):
    print(tabulate(controller.list_all_users(controller.cur),headers=['id_pengguna','username','nama','password','status']))     
    print (f"""---------------------------------------
         List Menu 
                  1.Hapus pengguna      3.Tambah pengguna      
                  2.Edit Pengguna       4.kembali   
          """)
    menu = helper.menu_input(4)
    
    if menu == 1 :
        id_pengguna = input('masukkan id pengguna untuk pengguna yang ingin dihapus : ')
        controller.delete_pengguna(controller.cur,id_pengguna)
        helper.clear()
        pengguna(status_login)
        
    elif menu ==  2  :
        id_pengguna = input("pilih  pengguna yang ingin di edit : ")
        data_lama = controller.get_pengguna(controller.cur,id_pengguna)
        username = input((data_lama[0][0] + ' :')) or data_lama[0][0]
        nama_pengguna = input((data_lama[0][1] + ' :')) or data_lama[0][1]
        password = input((data_lama[0][2] + ' :')) or data_lama[0][2]
        data_baru = [username,nama_pengguna,password]
        controller.edit_pengguna(controller.cur,id_pengguna,data_baru)
        
        
    elif menu == 3 :
        username = input("masukkan username : ")
        nama = input ("masukkan nama : ")
        password = input("masukkan password : ")
        data_baru = [username,nama,password]
        controller.tambah_pengguna(controller.cur,data_baru)
        helper.clear()
        pengguna(status_login)   
    elif menu == 4 :
        helper.clear()
        dashboard.dashboard(status_login)
    else :
        pengguna(status_login)
        
