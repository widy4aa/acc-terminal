import helpers as helper

conn = helper.conn
cur = conn.cursor()

def login(username,password):
     query = f"select p.username,p.nama_pengguna,p.password,r.nama_role from pengguna p join role r on p.id_role = r.id_role where username = '{username}' and password = '{password}' "
     cur.execute(query)
     data = cur.fetchall()
     return data