import pc_controller as controller
import helpers as helper
from tabulate import tabulate
import pelanggan_view as pelanggan 



def menu_pc(status_login):
    helper.clear()
    print("Data PC")
    print (tabulate(controller.select_laptop(controller.cur),headers=['id pc','merek pc','nama_pemilik']))
    print (f"""---------------------------------------
           List Menu 
                    1.Tambah      3.Kembali      
                    2.Edit           
            """)
    menu=helper.menu_input(3)
    if menu == 1:
        print("tambah")
        merek =input("merek laptop : ")
        print(tabulate(controller.list_pelanggan(controller.cur),headers=['id_pelanggan','nama_pelanggan']))
        id_pelanggan = input ("masukkan pemilik pilih (id): ")
        data_pc = [merek,id_pelanggan]
        controller.tambah_laptop(controller.cur,data_pc)
        menu_pc(status_login)  
    elif menu == 2:
        id_pc=input("Pilih Pc yang ingin di edit id : ")
        data_pc=helper.read_selection(controller.cur,id_pc,'id_pc','pc')
        data_baru= input(str(data_pc[0][1]) + ' : ') or data_pc[0][1]
        controller.edit_pc(controller.cur,data_pc[0][0],data_baru)
        menu_pc(status_login)
        
        
    elif menu == 3 : 
        pelanggan.menu_pelangggan(status_login)
        
        
    
    
