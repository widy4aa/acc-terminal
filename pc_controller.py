import psycopg2
import helpers as helper

conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

def select_laptop(cur):
    query = f"""
    select id_pc,nama_pc,nama_pelanggan
    from pc p join pelanggan pe
    on p.id_pelanggan = pe.id_pelanggan
    """
    cur.execute(query)
    data = cur.fetchall()
    return data
    
def tambah_laptop(cur,data_baru):
    query = f"""
    insert into pc (nama_pc,id_pelanggan)
    values ('{data_baru[0]}',{data_baru[1]})
    """
    cur.execute(query)
    conn.commit()
    
    
def list_pelanggan(cur):
    query = f"""
    select id_pelanggan,nama_pelanggan 
    from pelanggan
    order by id_pelanggan;
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def edit_pc(cur,id_pc,data_baru):
    query = f"""
    update pc
    set nama_pc = '{data_baru}'
    where id_pc = {id_pc}
    """
    cur.execute(query)
    conn.commit()
    