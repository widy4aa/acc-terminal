import psycopg2
import helpers as helper

conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

def get_pengguna (cur,id_pengguna):
    query = f"""
    select username,nama_pengguna,password
    from pengguna
    where id_pengguna = {id_pengguna}
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def list_all_users(cur) :
    query = f"""
        select id_pengguna,username,password,nama_role from pengguna p join role r
        on p.id_role = r.id_role 
        order by id_pengguna
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def delete_pengguna(cur,id_pengguna):
    query = f"""
        delete from pengguna
        where id_pengguna = {id_pengguna}
    """
    cur.execute(query)
    conn.commit()

def edit_pengguna(cur,id_pengguna,data_baru):
    #helper.dd(data_baru)
    query = f"""
        update pengguna
        set username = '{data_baru[0]}',
        nama_pengguna = '{data_baru[1]}',
        password ='{data_baru[2]}'
        where id_pengguna = {id_pengguna}
    """
    cur.execute(query)
    conn.commit()

def tambah_pengguna(cur,data_pengguna):
    query = f"""
        insert into pengguna 
        (username,nama_pengguna,password,id_role)
        values ('{data_pengguna[0]}','{data_pengguna[1]}','{data_pengguna[2]}',2)
    """
    cur.execute(query)
    conn.commit()