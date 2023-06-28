import mysql.connector
#import project1_frontend

def bankData():
        con = mysql.connector.connect(host="localhost",user="root",passwd="Password12*",database="project")
        cur=con.cursor()
       
        cur.execute("CREATE TABLE IF NOT EXISTS Bank(ACC_ID integer primary key AUTO_INCREMENT,Firstname text,Surname text,DoB text,Age text,Gender text,ACC_TYPE text,Mobile text)")
        con.commit()
        con.close()              
def addbankRec(ACC_ID,Firstname,Surname,DoB,Age,Gender,ACC_TYPE,Mobile):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="Password12*")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("INSERT INTO Bank VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(ACC_ID,Firstname,Surname,DoB,Age,Gender,ACC_TYPE,Mobile))
        con.commit()
        con.close() 
def viewData():
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="Password12*")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("select * from Bank")
        row=cur.fetchall()
        con.close()       
        return row
def deleteRec(ACC_ID):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="Password12*")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("DELETE FROM Bank WHERE ACC_ID=%s",(ACC_ID,))
        con.commit()
        con.close()         
def searchData(ACC_ID,Firstname,Surname,DoB,Age,Gender,Mobile,ACC_TYPE):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="Password12*")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("SELECT * FROM Bank WHERE ACC_ID=%s or Firstname=%s or Surname=%s or DoB=%s or Age=%s or Gender=%s or ACC_TYPE=%s or Mobile=%s",(ACC_ID,Firstname,Surname,DoB,Age,Gender,ACC_TYPE,Mobile))
        rows=cur.fetchall()
        con.close()        
        return rows
def dataUpdate(ACC_ID="",Firstname="",Surname="",DoB="",Age="",Gender="",ACC_TYPE="",Mobile=""):
        con = mysql.connector.connect(host="localhost",user="root",passwd="Password12*")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("UPDATE Bank SET ACC_ID=%s,Firstname=%s,Surname=%s,DoB=%s,Age=%s,Gender=%s,ACC_TYPE=%s,Mobile=%s WHERE ACC_ID=%s",(ACC_ID,Firstname,Surname,DoB,Age,Gender,ACC_TYPE,Mobile))
        con.commit()
        con.close()    