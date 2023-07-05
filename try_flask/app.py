from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)

#for rendering webpages use templates

@app.route('/')
def index():
    return render_template('index.html')

#for variables insertions

@app.route('/hello/<user_name>')
def greet_users(user_name):
    return 'Hello  %s' %user_name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' %postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' %revNo

#trailing / in /python/ is used to access it as both /python & /python/ 
# because it has become a canonical URL
# where as /flask will only be accessible using /flask not /flask/ 

@app.route('/flask')
def greet_flask():
    return 'Hello Flask'

@app.route('/python/')
def greet_python():
    return 'Hello Python'

#added a webpage 'about' in the web server

@app.route('/about/')
def about():
    return render_template('about.html')

#using concepts of URL BULIDING in FLASK

@app.route('/admin')
def greet_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def greet_guest(guest):
    return 'Hello %s' %guest

@app.route('/user/<user_name>')
def greet_user(user_name):
    if user_name == 'admin':
        return redirect(url_for('greet_admin'))
    else:
        return redirect(url_for('greet_guest', guest = user_name))

#trying flask HTTP Methods


@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name 

@app.route('/login',methods= ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))
    
#trying flask templates with parameters

@app.route('/hi/<user>')
def hello_user(user):
    return render_template('hello.html',name = user)

@app.route('/result/<int:score>')
def result_display(score):
    return render_template('result.html',marks = score)

#trying tabular data feeding in Flask
@app.route('/result/')
def result():
    dict = {
        'Physics' : 75,
        'Chemistry' : 70,
        'Maths' : 80,
        'Biology' : 65
    }
    return render_template('result.html', result = dict)