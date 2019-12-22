import pyodbc
import os
song_name = []
song_file = []
play_list = dict()
for file in os.listdir("F:/test"):
    song_name.append(str(file.replace('mp3','')))

for x,y in zip(os.listdir("F:/test"),song_name):
    play_list[x] = y

print('------------SONG NAME---------SONG FILE-----------')

for x in play_list:
    conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=servername;'
                              'Database=Songs_playlist;'
                              'Trusted_Connection=yes;')
    cursor = conn.cursor()
    insert_query = ("INSERT INTO songs_db (Song_name,Song_file) VALUES (?,?);")
    Values = [play_list[x],x]
    cursor.execute(insert_query,Values)
    cursor.execute('SELECT * FROM dbo.songs_db')
    conn.commit()
    conn.close()








