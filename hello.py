from flask import Flask, render_template
from flask.helpers import url_for
from markupsafe import Markup

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
    my_list = ['Menu 1', 'Menu 2', 'Menu 3']
    return render_template('register.html', email=default_email, menus=my_list)




if __name__ == '__main__':
    app.run(debug=True)