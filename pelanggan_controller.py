import psycopg2
import helpers as helper

conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

def select_data_pelanggan(cur):
    query =f"""
    select id_pelanggan,nama_pelanggan,no_telp,jalan ||' '|| kecamatan ||' '|| kabupaten as alamat 
    from pelanggan p join alamat a 
    on a.id_alamat = p.id_alamat
    """
    cur.execute(query)
    data = cur.fetchall()
    return data
    

# fitur pelanggan
def input_data_alamat(cur,values_alamat):
    query_insert_alamat = f"""
    insert into alamat (id_alamat,jalan, kecamatan, kabupaten)
    values ({values_alamat[0]},'{values_alamat[1]}','{values_alamat[2]}','{values_alamat[3]}')
    """
    cur.execute(query_insert_alamat)
    conn.commit()
    
  
def input_data_pelanggan(cur,values_pelanggan):
    query_insert_pelanggan = f""" 
    insert into pelanggan (nama_pelanggan, no_telp, id_alamat)
    values  ('{values_pelanggan[0]}','{values_pelanggan[1]}',{values_pelanggan[2]})
    """  
    cur.execute(query_insert_pelanggan)
    conn.commit()
    
def cari_id_alamat(cur):
    query = f"""
        select id_alamat from alamat order by id_alamat desc 
        limit 1 ;
    """
    cur.execute(query)
    data = cur.fetchall()
    return data


def read_pelanggan_selection(cur,id_pelanggan):
    query =f"""
    select id_pelanggan,nama_pelanggan,no_telp,jalan ||' '|| kecamatan ||' '|| kabupaten as alamat 
    from pelanggan p join alamat a 
    on a.id_alamat = p.id_alamat
    where id_pelanggan = {id_pelanggan}
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def update_pelanggan (cur,id_pelanggan,data_baru):
    query = f"""
    update pelanggan 
    set nama_pelanggan = '{data_baru[1]}',
        no_telp = '{data_baru[2]}'
    where id_pelanggan = {id_pelanggan}
    """
    cur.execute(query)
    conn.commit()
    
def update_alamat (cur,id_alamat,data_baru):
    query = f"""
    update alamat 
    set jalan = '{data_baru[1]}',
        kecamatan = '{data_baru[2]}',
        kabupaten = '{data_baru[3]}'
    where id_alamat = {id_alamat}
    """
    cur.execute(query)
    conn.commit()