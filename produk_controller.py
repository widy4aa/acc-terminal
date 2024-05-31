import psycopg2
import helpers as helper

conn = helper.conn
cur = conn.cursor()


def get_all_produk(cur):
    query = f"""
    select id_produk,nama_produk,harga,nama_jenis_produk
    from produk p join jenis_produk j
    on p.id_jenis_produk = j.id_jenis_produk
    """
    cur.execute(query)
    data = cur.fetchall()
    return data


def select_product(cur,id_produk):
    query = f"""
    select id_produk,nama_produk,harga,nama_jenis_produk
    from produk p join jenis_produk j
    on p.id_jenis_produk = j.id_jenis_produk
    where id_produk = {id_produk}
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def add_produk(cur,produk_baru):
    query = f"""
    insert into produk (nama_produk,harga,id_jenis_produk) 
    values ('{produk_baru[0]}','{produk_baru[1]}','{produk_baru[2]}')
    """    
    cur.execute(query)
    conn.commit()

def edit_produk(cur,id_produk,produk_baru):
    query = f"""
    update produk 
    set nama_produk = '{produk_baru[0]}',
        harga = {produk_baru[1]},
        id_jenis_produk = {produk_baru[2]}
    where id_produk = {id_produk}
    """
    cur.execute(query)
    conn.commit() 
    
def delete_produk(cur,id_produk):
    query = f"""
    delete produk 
    where id_produk = {id_produk}
    """
    cur.execute(query)
    conn.commit()
    

