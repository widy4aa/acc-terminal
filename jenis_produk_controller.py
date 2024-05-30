import helpers as helper

conn = helper.conn
cur = conn.cursor()

def get_all_jenis(cur):
    query = f"""
    select * from jenis_produk
    """
    cur.execute(query)
    data = cur.fetchall()
    return data
    
def get_select_jenis(cur,id_jenis):
    query = f"""
    select * from jenis_produk where id_jenis_produk = {id_jenis}
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def add_jenis(cur,data_baru):
    query = f"""
    insert into jenis_produk 
    (nama_jenis_produk) values ('{data_baru}')
    """
    cur.execute(query)
    conn.commit()
    
def update_jenis(cur,id_jenis,jenis_baru):
    query = f"""
    update jenis_produk
    set nama_jenis_produk = '{jenis_baru}'
    where id_jenis_produk = {id_jenis}
    """
    cur.execute(query)
    conn.commit()
    
def delete_jenis(cur,id_jenis):
    query = f"""
    delete from jenis_produk
    where id_jenis_produk = {id_jenis}
    """
    cur.execute(query)
    conn.commit()
    
