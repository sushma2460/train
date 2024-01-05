from flask import Flask,render_template,url_for,request
from markupsafe import escape
import mysql.connector


app=Flask(__name__)


db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sushma',
    database='ticket'
) 


cur=db.cursor(dictionary=True)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def index():
    cur.execute("select * from book")
    data=cur.fetchall()
    k=[]
    for i in data:
        print(i)
        dummy=[]
        dummy.append(i['FirstName'])
        dummy.append(i['LastName'])
        dummy.append(i['Email'])
        dummy.append(i['Section'])
        k.append(dummy)




    return render_template('home.html',data=k)


@app.route('/home',methods=['post'])
def formpage1():
    FirstName=request.form['FirstName']
    LastName=request.form['LastName']
    Email=request.form['Email']
    Section=request.form['Section']
    print(FirstName,LastName,Email,Section)
    sql="INSERT INTO book(FirstName,LastName,Email,Section) VALUES(%s,%s,%s,%s)"
    values=(FirstName,LastName,Email,Section)
    cur.execute(sql,values)
    db.commit()
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)