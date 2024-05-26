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
