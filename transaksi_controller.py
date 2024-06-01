import helpers as helper

conn = helper.conn
cur = conn.cursor()


def get_all_trx(cur):
    query = f"""
    select tr.id_transaksi,pel.nama_pelanggan,pe.nama_pengguna,mp.nama_metode_pembayaran,tr.tgl_dibuat,tr.keterangan
    from transaksi tr 
    join pengguna pe on tr.id_pengguna = pe.id_pengguna
    join role ro on ro.id_role = pe.id_role
    join metode_pembayaran mp on mp.id_metode_pembayaran = tr.id_metode_pembayaran
    join pelanggan pel on pel.id_pelanggan = tr.id_pelanggan 
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def get_all_trx_now(cur):
    query = f"""
    select tr.id_transaksi,pel.nama_pelanggan,pe.nama_pengguna,mp.nama_metode_pembayaran,tr.tgl_dibuat,tr.keterangan
    from transaksi tr 
    join pengguna pe on tr.id_pengguna = pe.id_pengguna
    join role ro on ro.id_role = pe.id_role
    join metode_pembayaran mp on mp.id_metode_pembayaran = tr.id_metode_pembayaran
    join pelanggan pel on pel.id_pelanggan = tr.id_pelanggan 
    where date(tgl_dibuat) = date(NOW())
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def get_all_trx_month(cur):
    query = f"""
    select tr.id_transaksi,pel.nama_pelanggan,pe.nama_pengguna,mp.nama_metode_pembayaran,tr.tgl_dibuat,tr.keterangan
	from transaksi tr 
    join pengguna pe on tr.id_pengguna = pe.id_pengguna
    join role ro on ro.id_role = pe.id_role
    join metode_pembayaran mp on mp.id_metode_pembayaran = tr.id_metode_pembayaran
    join pelanggan pel on pel.id_pelanggan = tr.id_pelanggan 
    where extract(month from tgl_dibuat) = extract(month from now())
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def detail_trx(cur,id_transaksi):
    query1 = f"""
    select pr.id_produk,pr.nama_produk,jp.nama_jenis_produk,pr.harga,dtp.kuantitas,(pr.harga * dtp.kuantitas) as "total"
    from transaksi tr 
    join pengguna pe on tr.id_pengguna = pe.id_pengguna
    join role ro on ro.id_role = pe.id_role
    join metode_pembayaran mp on mp.id_metode_pembayaran = tr.id_metode_pembayaran
    join detail_transaksi_produk dtp on dtp.id_transaksi = tr.id_transaksi
    join produk pr on pr.id_produk = dtp.id_produk
    join jenis_produk jp on jp.id_jenis_produk = pr.id_jenis_produk
    join pelanggan pel on pel.id_pelanggan = tr.id_pelanggan 
    where tr.id_transaksi = {id_transaksi}
    """
    cur.execute(query1)
    data1 = cur.fetchall()
    
    query2 =f"""
    select la.id_layanan,la.nama_layanan,la.harga,pc.nama_pc
    from transaksi tr 
    join pengguna pe on tr.id_pengguna = pe.id_pengguna
    join role ro on ro.id_role = pe.id_role
    join metode_pembayaran mp on mp.id_metode_pembayaran = tr.id_metode_pembayaran
    join detail_transaksi_layanan dtp on dtp.id_transaksi = tr.id_transaksi
    join layanan la on dtp.id_layanan = la.id_layanan
    join pelanggan pel on pel.id_pelanggan = tr.id_pelanggan
    join pc on dtp.id_pc = pc.id_pc 
    where tr.id_transaksi = {id_transaksi}
    """
    cur.execute(query2)
    data2 = cur.fetchall()
    
    query3 = f"""
    select tr.id_transaksi,pel.nama_pelanggan,pe.nama_pengguna,mp.nama_metode_pembayaran,tr.tgl_dibuat,tr.keterangan
    from transaksi tr 
    join pengguna pe on tr.id_pengguna = pe.id_pengguna
    join role ro on ro.id_role = pe.id_role
    join metode_pembayaran mp on mp.id_metode_pembayaran = tr.id_metode_pembayaran
    join pelanggan pel on pel.id_pelanggan = tr.id_pelanggan
    where tr.id_transaksi = {id_transaksi}
    """
    cur.execute(query3)
    header = cur.fetchall()

    data = [header,data1,data2]
    return data

def total_bayar(cur,id_transaksi):
    query1 = f"""
    select sum(pr.harga * dtp.kuantitas)
    from transaksi tr 
    join pengguna pe on tr.id_pengguna = pe.id_pengguna
    join role ro on ro.id_role = pe.id_role
    join metode_pembayaran mp on mp.id_metode_pembayaran = tr.id_metode_pembayaran
    join detail_transaksi_produk dtp on dtp.id_transaksi = tr.id_transaksi
    join produk pr on pr.id_produk = dtp.id_produk
    join jenis_produk jp on jp.id_jenis_produk = pr.id_jenis_produk
    join pelanggan pel on pel.id_pelanggan = tr.id_pelanggan 
    where tr.id_transaksi = {id_transaksi}
    """
    cur.execute(query1)
    data1 = cur.fetchall()
    
    query2 =f"""
    select sum(la.harga)
    from transaksi tr 
    join pengguna pe on tr.id_pengguna = pe.id_pengguna
    join role ro on ro.id_role = pe.id_role
    join metode_pembayaran mp on mp.id_metode_pembayaran = tr.id_metode_pembayaran
    join detail_transaksi_layanan dtp on dtp.id_transaksi = tr.id_transaksi
    join layanan la on dtp.id_layanan = la.id_layanan
    join pelanggan pel on pel.id_pelanggan = tr.id_pelanggan
    join pc on dtp.id_pc = pc.id_pc 
    where tr.id_transaksi = {id_transaksi}
    """
    cur.execute(query2)
    data2 = cur.fetchall()
    harga = data2[0][0] + data1[0][0]
    
    return harga
    

    