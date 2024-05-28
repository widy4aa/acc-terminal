import psycopg2

#ganti seusai database coi
conn = psycopg2.connect(database='Acc', user='postgres', password='dio', host='localhost', port=5432)
cur = conn.cursor()

# SELECT MATA KULIAH

# def read_mata_kuliah(cur):    
#     query = "SELECT * FROM mata_kuliah"
#     cur.execute(query)
#     data = cur.fetchall()
#     for i in data:
#         print(i)
#     # cur.close()
#     # conn.close()

def read_table(cur,table):
    query = f"select * from {table}"
    cur.execute(query)
    data = cur.fetchall()
    return data
    
print(read_table(cur,'role'))
    

# # SELECT SEMESTER
# # query = "SELECT * FROM semester"
# # cur.execute(query)
# # data = cur.fetchall()
# # for i in data:
# #     print(i)
# # cur.close()
# # conn.close()

# # DYNAMIC INSERT DATA
# # total_input = int(input(f"Mau menambahkan berapa data?: "))

# # for i in range(total_input):
# #     nama_mata_kuliah = input(f"Masukkan nama mata kuliah: ")
# #     sks = int(input(f"Masukkan jumlah sks: "))
# #     semester_id = int(input(f"Masukkan semester: "))
# #     query = f"INSERT INTO mata_kuliah(nama_mata_kuliah, sks, semester_id) VALUES('{nama_mata_kuliah}', {sks}, {semester_id})"
# #     # query = f"INSERT INTO mata_kuliah(nama_mata_kuliah, sks, semester_id) VALUES(%s, %s, %s)"
# #     cur.execute(query, (nama_mata_kuliah, sks, semester_id))

# # conn.commit()

# # read_mata_kuliah(cur)
# # cur.close()
# # conn.close()

# # UPDATE
# nama_mata_kuliah = input(f"Masukkan nama mata kuliah: ") or data2[1]
# sks = input(f"Masukkan jumlah sks: ") or data2[2]
# sks = int(sks)
# semester_id = input(f"Masukkan semester: ") or data2[3]

# query_update = f"UPDATE mata_kuliah SET nama_mata_kuliah = '{nama_mata_kuliah}', sks = {sks}, semester_id = {semester_id} WHERE id_mata_kuliah = {id_mata_kuliah}"

# # -- Manipulasi string
# # cur.execute(query_update, (nama_mata_kuliah, sks, semester_id, id_mata_kuliah))

# # -- Fstring
# cur.execute(query_update)

# conn.commit()
# print(f"total baris yang diubah: {cur.rowcount}")

# cur.close()
# conn.close()

read_mata_kuliah(cur)
id_mata_kuliah = input('Masukkan id mata kuliah yang ingin dihapus: ')
query_delete = f"DELETE FROM mata_kuliah WHERE id_mata_kuliah = {id_mata_kuliah}"
cur.execute(query_delete)
print(f"total baris yang dihapus: {cur.rowcount}")
conn.commit()

