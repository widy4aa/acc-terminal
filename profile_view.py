import helpers as helper
import profile_controller as controller
import dashboard_view as dashboard

dump = [('Almashuda34', 'Huda', 'huda34678', 'owner')]

def menu_profile (status_login) :
    print ('---------------------')
    print (f"username :{status_login[0][1]}")
    print (f"Nama :{status_login[0][2]}")
    print (f"Status :{status_login[0][3]}")
    print (f"""---------------------------------------
           List Menu 
                    1.Ganti Password      3.Kembali      
                    2.List All User           
            """)
    menu=helper.menu_input(3)
    
    if menu == 1 :
        print("ganti password : ")
        menu_profile (status_login)
        
    elif menu == 2 :     
        menu_profile (status_login)
        
    elif menu == 3 :
        dashboard.dashboard(status_login)
        
    
    
    
menu_profile(dump)