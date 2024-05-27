import psycopg2
import os

conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

def clear():
    if os.name == 'posix': # jika os tipe unix
        os.system('clear')
    elif os.name == 'nt': # jika os tipe windows
        os.system('cls')
    else:
        print("Sistem operasi tidak didukung.")
        
def read_jumlah_data(cur,table):
    query = f"SELECT count(*) FROM {table} WHERE DATE(tgl_dibuat) = DATE(NOW());"
    cur.execute(query)
    data = cur.fetchall()
    return data