import helpers as helper

conn = helper.conn 
cur = conn.cursor()

def read_jumlah_data(cur,table):
    query = f"SELECT count(*) FROM {table} WHERE DATE(tgl_dibuat) = DATE(NOW());"
    cur.execute(query)
    data = cur.fetchall()
    return data

def read_jumlah_uang_masuk(cur):
    query1 = f"""select sum(harga*dt.kuantitas) from transaksi t 
                join detail_transaksi_produk dt on dt.id_transaksi = t.id_transaksi 
                join produk p on p.id_produk = dt.id_produk WHERE DATE(tgl_dibuat) = DATE(NOW());""" 
    
    query2 = f"""select sum(harga) from transaksi t 
                join detail_transaksi_layanan dt on dt.id_transaksi = t.id_transaksi 
                join layanan l on l.id_layanan = dt.id_layanan WHERE DATE(tgl_dibuat) = DATE(NOW());""" 
    
    cur.execute(query1)
    data1 = cur.fetchall()
    cur.execute(query2)
    data2 = cur.fetchall()
    
    if data1[0][0] == None :
        uang_di_produk = 0
    else :
        uang_di_produk = data1[0][0]
    if data2[0][0] == None :
        uang_di_layanan = 0
    else :
        uang_di_layanan = data2[0][0]
    
    uang = int(uang_di_layanan) + int(uang_di_produk)
    return uang
    
def produk_layanan_diminati (cur): 
    query1 = f"""SELECT p.nama_produk, COUNT(*) as total_transaksi FROM transaksi t 
                JOIN detail_transaksi_produk dt ON dt.id_transaksi = t.id_transaksi 
                JOIN produk p ON p.id_produk = dt.id_produk WHERE DATE(tgl_dibuat) = DATE(NOW()) 
                GROUP BY p.nama_produk ORDER BY total_transaksi DESC LIMIT 1;""" 
    query2 = f"""SELECT l.nama_layanan, COUNT(*)  as total_transaksi FROM transaksi t 
                JOIN detail_transaksi_layanan dt ON dt.id_transaksi = t.id_transaksi 
                JOIN layanan l ON l.id_layanan = dt.id_layanan WHERE DATE(tgl_dibuat) = DATE(NOW()) 
                GROUP BY l.nama_layanan ORDER BY total_transaksi DESC LIMIT 1;""" 
    cur.execute(query1)
    data1 = cur.fetchall()
    cur.execute(query2)
    data2 = cur.fetchall()
    
    
    if data1:
        jumlah_trx_produk = data1[0][1]
    else :
        jumlah_trx_produk = 0
    if data2:
        jumlah_trx_layanan = data2[0][1]
    else :
        jumlah_trx_layanan = 0
 
    if jumlah_trx_produk > jumlah_trx_layanan : 
        diminati = data1[0][0]
    elif jumlah_trx_produk < jumlah_trx_layanan :
        diminati = data2[0][0]
    elif jumlah_trx_layanan == jumlah_trx_produk == 0 :
        diminati = "Belum Ada"
    else  :
            diminati = f"{data1[0][0] or 0} dan {data2[0][0] or 0}"
    return diminati

def metode_pembayaran_diminati(cur):
    query = f""" select mp.nama_metode_pembayaran from transaksi t 
                join metode_pembayaran mp on mp.id_metode_pembayaran = t.id_metode_pembayaran 
                group by mp.nama_metode_pembayaran order by mp.nama_metode_pembayaran asc limit 1;"""
    cur.execute(query)
    data = cur.fetchall()
    return data

def menu_dashboard_input():
    menu = int(input("pilih berdasarkan nomor :"))
    if 1 <= menu <=8 :
        return menu
    else : 
        menu_dashboard_input()
        
def searching_pelanggan(cur,inputan):
    query =f"""
    select id_pelanggan,nama_pelanggan,jalan || kecamatan || kabupaten as alamat 
    from pelanggan p join alamat a 
    on a.id_alamat = p.id_alamat
    where nama_pelanggan ilike '%{inputan}%';
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def searching_produk (cur,inputan):
    query =f"""
    select id_produk,nama_produk,harga,j.nama_jenis_produk
    from  produk p join jenis_produk j
    on p.id_jenis_produk = j.id_jenis_produk  
    where nama_produk ilike '%{inputan}%';
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

