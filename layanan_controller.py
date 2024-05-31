import helpers as helper

conn = helper.conn
cur = conn.cursor()

def get_all_layanan(cur):
    query = f"""
    select * from layanan
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def get_selection_layanan(cur,id_layanan):
    query = f"""
    select * from layanan 
    where id_layanan = {id_layanan}
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def tambah_layanan(cur,data_baru):
    query =  f"""
    insert into layanan (nama_layanan,harga)
    values ('{data_baru[0]}',{data_baru[1]})
    """
    cur.execute(query)
    conn.commit()
    
def edit_layanan(cur,data_baru,id_layanan):
    query = f"""
    update layanan 
    set nama_layanan = '{data_baru[0]}',
        harga = {data_baru[1]}
    where id_layanan = {id_layanan}
    """
    cur.execute(query)
    conn.commit()

def delete_layanan(cur,id_layanan):
    query = f"""
    delete from layanan
    where id_layanan = {id_layanan}
    """
    cur.execute(query)
    conn.commit()