from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse, abort
import sqlite3 as sql

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
  return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #fetch user data
        accountDetails = request.form
        name = accountDetails['signup_name']
        email = accountDetails['signup_email']
        password = accountDetails['signup_password']
        cnf_password = accountDetails['signup_cnf_password']

        try:
            if password == cnf_password:
                with sql.connect("account_database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO accounts (name,email,password) VALUES (?,?,?)",(name,email,password) )
                    con.commit()
                    msg = 'Record successfully added!<br><a href="./login">Login Page</a>'
            else :
                msg = 'Password and Comfirm Password mis-matched<br><a href="./signup">Go Back</a>'
        except:
            con.rollback()
            msg = 'Error in INSERT Operation<br><a href="./signup">Go Back</a>'
        finally:
            return msg;
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #fetch user data
        accountDetails = request.form
        email = accountDetails['log_email']
        password = accountDetails['log_password']
        cnf_password = accountDetails['log_cnf_password']

        try:
            if password == cnf_password:
                with sql.connect("account_database.db") as con:
                    cur = con.cursor()
                    result = cur.execute("SELECT * FROM accounts WHERE email=? AND password=?", (email,password))
                    if result:
                        msg = 'Login successfull!<br><a href="./homepage">Go to HomePage</a>'
            else :
                msg = 'Password and Comfirm Password mis-matched<br><a href="./login">Go Back</a>'
        except:
            con.rollback()
            msg = 'Error in SELECT Operation<br><a href="./login">Go Back</a>'
        finally:
            return msg;
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)