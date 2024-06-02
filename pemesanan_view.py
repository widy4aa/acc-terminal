import pemesanan_controller as controller
import dashboard_view as dashboard
from tabulate import tabulate
import pelanggan_controller as pel_controller
import helpers as helper
import produk_controller as per_controller
import layanan_controller as la_controller
import pc_controller as pc_controller
import dashboard_view as dashboard

#dump_detail =[(1, 'Almashuda34', 'Huda', 'huda34678', 1), (1, 'Widya', '085230369011', 'Jl. Merdeka No. 123 Wuluhan Jember'), [[1, ' Asus Rog Strix Nvidia RTX 3060 TI', 16000000, 'GPU', '2', 32000000], [2, 'Intel i3 1200f', 1200000, 'CPU', '2', 2400000], [3, 'Amd Ryzen 5 5600G', 120000, 'CPU', '4', 480000]], [[1, 'Install ulang Windwos', 750000, 'Asus X441UV'], [3, 'Storage Recovery', 250000, 'Asus X441UV']], 'skjdasd', 'cash', 35880000]

def detail(data):
    print (f"""
    pembuat        : {data[0][2]}
    nama pelanggan : {data[1][1]}
    
produk yang di beli :

{tabulate(data[2],headers=['id_produk','nama produk','harga','jenis','kuantitas','total harga per barang'])}

layanan yang di beli :

{tabulate(data[3],headers=['id_layanan','nama layanan','harga','nama laptop','id laptop'])}

keterangan        : {data[4]}
metode pembayaran : {data[5]}
total bayar       : {data[6]}

           """)

def menu_pemesanan(status_login):
    data_pemesanan_all = []
    print("--------------")
    data_pelanggan =  pel_controller.select_data_pelanggan(helper.cur)
    print(tabulate(data_pelanggan,headers=['id_pelanggan','nama_pelanggan','no_telp','alamat']))
    id_pelanggan = input("pilih id pelanggan yang ingin memesan : ")
    data_pembeli = pel_controller.read_pelanggan_selection(helper.cur,id_pelanggan)
    data_pemesanan_all.append(data_pembeli)
    helper.clear()
    print(tabulate(data_pembeli,headers=['id_pelanggan','nama_pelanggan','no_telp','alamat']))
    data_produk_dibeli = []
    data_produk = per_controller.get_all_produk(helper.cur)
    while True:
        helper.clear()
        print(tabulate(data_produk,headers=['id_produk','nama_produk','harga','jenis']))
        id_produk = input("pilih id_produk jika tidak pilih 0 : ")
        kuantitas = input("pilih kuantitas jika tidak pilih 0 :")
        if id_produk != "0" and kuantitas != "0":
            data = [id_produk,kuantitas]
            data_produk_dibeli.append(data)
        beli_lagi = input("tekan y jika ingin menambah pesanan : ")
        if beli_lagi != "y":
            break
    data_pemesanan_all.append(data_produk_dibeli)          
    data_layanan = la_controller.get_all_layanan(helper.cur)
    data_pc = pc_controller.select_laptop_pelanggan(helper.cur,id_pelanggan)
    data_layanan_dibeli = [] 
    while True:
        helper.clear()
        print(tabulate(data_layanan,headers=['id_layanan','nama layanan','harga']))
        print (tabulate(data_pc,headers=['id pc','merek pc','nama_pemilik']))
        
        id_layanan = input("pilih id layanan jika tidak 0 : ")
        id_pc = input("pilih id pc jika tidak 0 : ")
        if id_layanan != "0" and id_pc != "0":
            data2 = [id_layanan,id_pc]
            data_layanan_dibeli.append(data2)
        beli_lagi = input("tekan y jika ingin menambah pesanan : ")
        if beli_lagi != "y":
            break
    data_pemesanan_all.append(data_layanan_dibeli)      
    metode_pembayaran = input("masukkan metode_pembayaran 1(cash)/2(debit): ")   
    keterangan = input("masukkan keterangan : ")
    pembuat = controller.liat_pembuat(helper.cur,status_login[0][0])
    data_pemesanan_all.append(metode_pembayaran)
    data_pemesanan_all.append(keterangan)
    data_pemesanan_all.append(pembuat)
    
    data = controller.struk(helper.cur,data_pemesanan_all)
    helper.clear()
    print(detail(data))
    pembelian = input("tekan y untuk konfirmasi transaksi dan pembayaran : ")
    if pembelian == 'y':
        controller.pembelian(helper.cur,data)

    helper.clear()
    dashboard.dashboard(status_login)    
    

    