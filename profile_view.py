import helpers as helper
import profile_controller as controller
import login_view as login 
from tabulate import tabulate

# dump = [('Almashuda34', 'Huda', 'huda', 'owner')]

def ganti_pass(status_login):
    pass_lama = input("pass lama (enter jika ): ")
    if pass_lama == status_login[0][2] :
        pass_baru = input("masukkan pass_baru : ")
        controller.ganti_password(controller.cur,status_login[0][0],pass_baru)
        input("Tekan enter untuk keluar dan jalankan ulang program")
        exit()
    elif pass_lama == "":
        menu_profile(status_login)
    else :
        ganti_pass(status_login)
        

def menu_profile (status_login) :
    print ('---------------------')
    print (f"username :{status_login[0][0]}")
    print (f"Nama :{status_login[0][1]}")
    print (f"Status :{status_login[0][3]}")
    print (f"""---------------------------------------
           List Menu 
                    1.Ganti Password      3.Kembali      
                    2.List All User           
            """)
    menu=helper.menu_input(3)
    
    if menu == 1 :
        ganti_pass(status_login)
        
        
    elif menu == 2 :
        helper.clear()
            
    
    elif menu == 3 :
        import dashboard_view as dashboard
        dashboard.dashboard(status_login)
        
    
    
# menu_profile(dump)