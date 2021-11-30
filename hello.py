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
    return """
    <h2>Login Page</h2>
    Or goto <a href="%s">profile page</a>
    """ % url_for('profile_page', username='Aris')

@app.route('/product')
def product_page():
    content = Markup("<h1>Product</h1>")
    title = "Product Page"
    return render_template('hello.html', 
        content=content, title=title)




if __name__ == '__main__':
    app.run(debug=True)