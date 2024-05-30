import helpers as helper
import produk_controller as controller
from tabulate import tabulate

dump = [('Almashuda34', 'Huda', 'huda34678', 'owner')]

def menu_produk (status_login):
    print("----------------------------")
    data_produk = controller.get_all_produk(controller.cur)
    print(tabulate(data_produk,headers=['id_produk','nama_produk','harga','jenis']))
    

menu_produk(dump)