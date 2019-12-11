from flask import Flask, redirect, request, url_for, render_template
import cx_Oracle

app = Flask(__name__)
# con = cx_Oracle.connect('username/password@localhost')
# cursor = cx_Oracle.cursor()
# os.environ.get("SECRET_KEY") or

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',title="Home")

@app.route("/post")
def each_post():
    return render_template('blog-details.html',title="Post")

@app.route("/archive")
def archive():
    return render_template('archive.html',title="Archive")

@app.route("/Contact")
def contact():
    return render_template('contact.html',title="Contact")

@app.route("/Category")
def each_category():
    return render_template('category.html', title="Category")


if __name__ == "__main__":
    app.run(debug=True)

