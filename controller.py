import psycopg2

#ganti seusai database coi
conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

def login(username,password):
     query = f"select * from pengguna where username = '{username}' and password = '{password}' "
     cur.execute(query)
     data = cur.fetchall()
     return data

# print(login(user))

def read_table(cur,table):
    query = f"select * from {table}"
    cur.execute(query)
    data = cur.fetchall()
    return data

#print(read_table(cur,'pengguna'))


def read_selection_table(cur,table,column,selection):
    query =f"select * from {table} where {column}={selection}"
    cur.execute(query)
    data = cur.fetchall()
    return data