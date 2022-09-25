from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

#Config DB
# db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '*******'  #enter mysql password
app.config['MYSQL_DB'] = 'flask_app'


mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #fetch user data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        print(cur)
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return 'Success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)