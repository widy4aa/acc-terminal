import helpers as helper
import produk_controller as p_controller
import layanan_controller as la_controller
import pc_controller as pc_controller

conn =  helper.conn
cur = helper.cur
dump_pemesanan = [(1, 'Almashuda34', 'Huda', 'huda34678', 1), (1, 'Widya', '085230369011', 'Jl. Merdeka No. 123 Wuluhan Jember'), [[2, 'Intel i3 1200f', 1200000, 'CPU', '2', 2400000]], [[1, 'Install ulang Windwos', 750000, 'Asus X441UV', '1'], [2, 'Repasta', 75000, 'Asus X441UV', '1']], '1', 'cash', 3225000]
dump_pemesanan_lama = [[(1, 'Widya', '085230369011', 'Jl. Merdeka No. 123 Wuluhan Jember')], [['1', '1']], [['1', '1'],['2','1']], '1', '1', [(1, 'Almashuda34', 'Huda', 'huda34678', 1)]]


def liat_pembuat(cur,username):
    query = f"""select * from pengguna where username = '{username}'"""
    cur.execute(query)
    data = cur.fetchall()
    return data

def struk(cur,data_pemesanan):
    data_pelanggan = data_pemesanan[0][0]
    data_produk_dibeli = data_pemesanan[1]
    data_layanan_dibeli = data_pemesanan[2]
    data_meotode_pembayaran = data_pemesanan[3]
    data_transaksi_keterangan = data_pemesanan[4]
    data_pembuat = data_pemesanan[5][0]
    total_bayar = 0
    
    data_produk_lengkap = []
    for i in data_produk_dibeli :
        i[0] = p_controller.select_product(helper.cur,i[0])
        data_produk = []
       # print(i,"--")
        for data_produk_list in i[0][0]:
            #data_produk.append(i[1]) 
            data_produk.append(data_produk_list)
           # data_produk.append(i[1])
        total = int(i[0][0][2])*int(i[1])
        total_bayar += total
        data_produk.append(i[1])
        data_produk.append(total)
        data_produk_lengkap.append(data_produk)
        
        
    #helper.dd(data_produk_lengkap)
    
    
    data_layanan_lengkap = []
    for i in data_layanan_dibeli:
        i[0] = la_controller.get_selection_layanan(helper.cur,i[0])
        id_laptop = i[1]
        i[1]= pc_controller.select_laptop_id(helper.cur,i[1])
        i[1] = i [1][0][0]
        data_layanan = []
        for data_layanan_list in i[0][0]:
            data_layanan.append(data_layanan_list)
        data_layanan.append(i[1])
        data_layanan.append(id_laptop)
        data_layanan_lengkap.append(data_layanan)
        total_bayar += (i[0][0][2])
    
    if data_meotode_pembayaran == '1' :
        data_meotode_pembayaran = 'cash'
    elif data_meotode_pembayaran == '2' :
        data_meotode_pembayaran = 'debit'
    
    data = [data_pembuat,data_pelanggan,data_produk_lengkap,data_layanan_lengkap,data_transaksi_keterangan,data_meotode_pembayaran,total_bayar]
    
    return data
 
def get_id_transaksi(cur):
    query = f"""
    select id_transaksi 
    from transaksi 
    order by id_transaksi desc 
    limit 1;
    """ 
    cur.execute(query)
    data = cur.fetchall()
    return data [0][0]

def get_id_pc(cur):
    query = f"""
    select id_transaksi 
    from transaksi 
    order by id_transaksi desc 
    limit 1;
    """ 
    cur.execute(query)
    data = cur.fetchall()
    return data [0][0]
    

    
    
def pembelian (cur,pemesanan):
        
    
    #inser trx 
    keterangan = pemesanan [4]
    id_pengguna = pemesanan[0][0]
    id_pelanggan = pemesanan[1][0]
    metode_pembayaran = pemesanan[5]
    if metode_pembayaran == "cash" :
        id_metode_pembayaran = 1
    else :    
        id_metode_pembayaran = 2

    query = f"""
    insert into transaksi (keterangan,tgl_dibuat,id_pengguna,id_pelanggan,id_metode_pembayaran)
    values ('{keterangan}',date(now()),{id_pengguna},{id_pelanggan},{id_metode_pembayaran})
    """
    cur.execute(query)
    conn.commit()
    
    
    id_trx = get_id_transaksi(cur)
    
    
    #insert produk 
    if pemesanan[2] != [] :
        for i in pemesanan[2] :
            kuantitas = i[4]
            id_produk = i[0]
            query2 = f"""
                insert into detail_transaksi_produk (kuantitas,id_transaksi,id_produk)
                 values ({kuantitas},{id_trx},{id_produk})
            """
            cur.execute(query2)
            conn.commit()
                
   # insert layanan


    if pemesanan[3] != [] :
        for i in pemesanan[3] :
            id_pc = int(i[4])
            id_layanan = i[0]
            query2 = f"""
                insert into detail_transaksi_layanan (id_transaksi,id_pc,id_layanan)
                values {id_trx,id_pc,id_layanan}
            """
            cur.execute(query2)
            conn.commit()
            
    
        

