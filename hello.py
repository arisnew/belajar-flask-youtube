from flask import Flask, render_template, request
from flask.helpers import url_for
from markupsafe import Markup
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello World!!!</h1>"

@app.route("/profile")
@app.route("/profile/<username>")
def profile_page(username=''):
    return "<h2>Profile Page %s</h2>" % username

@app.route('/login', methods=['POST', 'GET'])
def login_page():
    return render_template('login.html')

@app.route('/product')
def product_page():
    content = Markup("<h1>Product</h1>")
    title = "Product Page"
    return render_template('hello.html', 
        content=content, title=title)

@app.route('/register')
def register_page():
    default_email = 'aris@gmail.com'
    # my_list = ['Menu 1', 'Menu 3']
    return render_template('register.html',
        email=default_email,
        # menus=my_list
        )

@app.route('/proses-register', methods=['POST'])
def proses_register():
    # print(request.form)
    # connect
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='flask01data',
        )

        cur = conn.cursor()
        query_insert = "INSERT INTO user (nama, email, password) VALUES (%s, %s, %s)"
        cur.execute(query_insert, (
            request.form['nama'],
            request.form['email'],
            request.form['password'],
            ))
        conn.commit()
        cur.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            return 'gagal'
    else:
        conn.close()
    
    # result = ''
    # for k,v in request.form.items():
    #     result += '%s: %s<br/>'%(k,v)
    return 'ok'





if __name__ == '__main__':
    app.run(debug=True)