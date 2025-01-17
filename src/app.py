from flask import Flask,render_template,request,redirect,url_for,flash
from dotenv import load_dotenv
import os
from flask_mysqldb import MySQL

load_dotenv()


app=Flask(__name__)
app.config['MYSQL_HOST']=os.getenv('MYSQL_HOST')
app.config['MYSQL_USER']=os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD']=os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB']=os.getenv('MYSQL_DB')
app.secret_key=os.getenv('SECRET_KEY')

mysql=MySQL(app)


@app.route('/')
def index():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts')
    data=cursor.fetchall()
    print(data)
    return render_template('index.html',contacts=data)

@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method=='POST':
        fullname=request.form.get('fullname')
        phone=request.form.get('phone')
        email=request.form.get('email')

        cursor=mysql.connection.cursor()
        cursor.execute('INSERT INTO contacts (fullname,phone,email) VALUES (%s,%s,%s)',(fullname,phone,email))

        mysql.connection.commit()
        flash('Contact Added Succesfuly')
        
        return redirect(url_for('index'))
    
    
    
    return 'ADD contact'

@app.route('/edit')
def edit():
    return 'edit contact'

@app.route('/update')
def update():
    return 'update contact'

@app.route('/delete')
def delete():
    return 'delete contact'






if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')