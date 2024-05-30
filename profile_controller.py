import helpers as helper

conn = helper.conn
cur = conn.cursor()

def ganti_password(cur,username,pasword_baru):
    query = f"""
    update pengguna
    set password = '{pasword_baru}'
    where username = '{username}'
    """
    cur.execute(query)
    conn.commit()
    

    

