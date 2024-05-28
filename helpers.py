import os
import psycopg2

conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

# fungsi untuk clear console untuk bisa berfungsi di 2 tipe Sistem operasi
def clear():
    if os.name == 'posix': # jika os tipe unix
        os.system('clear')
    elif os.name == 'nt': # jika os tipe windows
        os.system('cls')
    else:
        print("Sistem operasi tidak didukung.")

# adalah singkatan dari dump die, yang dimana merupakan fungsi untuk menampilkan isi variable dan mematikan 
def dd(data):
    print(data)
    exit()




def menu_input(count_menu):
    menu = int(input("pilih berdasarkan nomor :"))
    if 1 <= menu <=count_menu :
        return menu
    else : 
        menu_input(count_menu)

# query_general    
def searching (cur,inputan,table,kolom):
    query =f"""
    select * 
    from {table} 
    where {kolom} ilike '%{inputan}%';     
    """ 
    cur.execute(query)
    data = cur.fetchall()
    return data

def read_selection (cur,selection,kolom,table):
    query = f"""
    select * from {table}
    where {kolom} = {selection}
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

