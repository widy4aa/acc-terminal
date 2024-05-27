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
    