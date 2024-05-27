import controller as controller
from tabulate import tabulate

def menu_dashboard_input():
    menu = int(input("pilih berdasarkan nomor :"))
    if 1 <= menu <=8 :
        return menu
    else : 
        menu_dashboard_input()
        
#searching 
def searching_dashboard (): 
    inputan = input("cari :")
    data_pelanggan=controller.searching_pelanggan(controller.cur,inputan)
    data_produk=controller.searching_produk(controller.cur,inputan)
    data_layanan=controller.searching(controller.cur,inputan,"layanan","nama_layanan")
    print("\n")
    print("dari pelanggan")
    print(tabulate(data_pelanggan,headers=['id_pelanggan','nama_pelanggan','alamat']))
    print("\n")
    print("dari layanan")
    print(tabulate(data_layanan,headers=['id_layanan','nama_layanan','harga']))
    print("\n")
    print("dari produk")
    print(tabulate(data_produk,headers=['id_layanan','nama_produk','harga','jenis']))
    
    
#menu pelanggan 
def menu_pelanggan_input():
    menu = int(input("pilih berdasarkan nomor :"))
    if 1 <= menu <=4 :
        return menu
    else : 
        menu_pelanggan_input()
        
def menu_pelangggan():
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
        
    
        

        

        
    
    

