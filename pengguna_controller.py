import psycopg2
import helpers as helper

conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

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


