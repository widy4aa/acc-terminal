import psycopg2
import helpers as helper

conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

def ganti_password(cur,username,pasword_baru):
    query = f"""
    update pengguna
    set password = '{pasword_baru}'
    where username = '{username}'
    """
    cur.execute(query)
    conn.commit()
    

    

