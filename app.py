from flask import Flask,render_template,request,redirect,session
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
app=Flask(__name__)
app.secret_key="secret123"
def init_db():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Username TEXT,
                   Email TEXT,
                   Password TEXT)""")
    conn.commit()
    conn.close()
init_db()
@app.route('/')
def home():
    return redirect('/login')
@app.route('/register', methods=['GET', 'POST'])
def register():
    message=None
    if request.method=='POST':
        Username=request.form['Username']
        Email=request.form['Email']
        Password=generate_password_hash(request.form['Password'])
        conn=sqlite3.connect("users.db")
        cursor=conn.cursor()
        cursor.execute("INSERT INTO users (Username,Email,Password)VALUES(?,?,?)",
                       (Username,Email,Password))
        conn.commit()
        conn.close()
        message="User Registred Successfully"
        return redirect('/login')
    return render_template('register.html' ,message=message)
@app.route('/login',methods=['GET','POST'])
def login():
    message=None
    if request.method=='POST':
        Username=request.form['Username']
        Password=request.form['Password']
        conn=sqlite3.connect("users.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM users WHERE Username=?",(Username,))
        user=cursor.fetchone()
        conn.close()
        if user and check_password_hash(user[3],Password):
            session['user']=Username
            return redirect('/dashboard')
        else:
            message="invalid username or password"
    return render_template('login.html',message=message)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html',user=session['user'])
    else:
        message="please Login First"
        return redirect('/login',message=message)
@app.route('/users')
def users():
    conn=sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute("SELECT Username,Email FROM users")
    all_users=cursor.fetchall()
    conn.close()
    return render_template('users.html',users=all_users)
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/login')
if __name__=="__main__":
    app.run(debug="True")