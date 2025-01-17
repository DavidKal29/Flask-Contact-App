from flask import Flask
from dotenv import load_dotenv
import os
from flask_mysqldb import MySQL

load_dotenv()


app=Flask(__name__)

@app.route('/')
def index():
    return 'Mula Hondo'

@app.route('/add_contact')
def add_contact():
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