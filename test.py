import sqlite3
from models.faces import Faces


def add_face(a):
    query = "insert into faces (id , full_name , file_name , group_id) values ( null , ? , ? , ? )"
    conn = sqlite3.connect("faces.db")
    conn.execute(query , (a.getFullName() , a.getFileName() , a.getGroup()))
    conn.commit()
    conn.close()

def getPaths():
    query = "select * from faces"
    conn = sqlite3.connect("faces.db")
    cursor  =  conn.execute(query)
    arr = list()
    for row in cursor:
        arr.append(row[2])
    conn.commit()
    conn.close()
    return arr

def getNameByPath(path):
    query = "select * from faces where file_name = '"+path+"'"
    conn = sqlite3.connect("faces.db")
    cursor  =  conn.execute(query)
    name = cursor.fetchone()
    conn.close()

    return name[1]
