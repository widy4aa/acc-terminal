import pengguna_controller as controller
import dashboard_view as dashboard
import helpers as helper
from tabulate import tabulate


dump = [('Almashuda34', 'Huda', 'huda34678', 'owner')]

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
        pengguna(status_login)
        
    elif menu ==  2  :
        print ("edit pengguna")
    elif menu == 3 :
        print ("tambah ppengguna")
    elif menu == 4 :
        helper.clear()
        dashboard.dashboard(status_login)
    else :
        pengguna(status_login)
        
pengguna(dump)