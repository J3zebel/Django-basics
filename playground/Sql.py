import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dcsmat",
    database="datad",
)


cursor = con.cursor()

def insert_data(user):
    cursor.execute("insert into user_tbl(username,email,passw) values (%s,%s,%s)",
                   (user.getusername(),
                    user.getEmailId(),
                    user.getPassword(),
                    ))
    con.commit()


def select_data():
    cursor.execute("select * from user_tbl")
    rows =  cursor.fetchall()
    for row in rows:
        print(row)
