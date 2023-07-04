from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

#for rendering webpages use templates

@app.route('/')
def index():
    return render_template('index.html')

#for variables insertions

@app.route('/hello/<user_name>')
def greet_user(user_name):
    return 'Hello  %s' %user_name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' %postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' %revNo


