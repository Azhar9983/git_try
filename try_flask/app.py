from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Home.html/')
def home_webpage():
    return redirect(url_for("home"))


@app.route('/gallary/')
def gallary():
    return render_template("gallary.html")

@app.route('/gallary.html/')
def gallary_webpage():
    return redirect(url_for("gallary"))


@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/about.html/')
def about_webpage():
    return redirect(url_for("about"))


@app.route('/result/')
def result():
    dict = {
        'Physics' : 75,
        'Chemistry' : 70,
        'Maths' : 80,
        'Biology' : 65
    }
    return render_template('result.html', result = dict)

@app.route('/result.html/')
def result_webpage():
    return redirect(url_for('result'))


@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/index.html/')
def index_webpage():
    return redirect(url_for("index"))


@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/contact.html/')
def contact_webpage():
    return redirect(url_for("contact"))


#-----------------------------------------------------------------
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


@app.route('/success/<name>')
def success(name):
    return 'Looged in as %s' %name 

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/validate/', methods = ['POST'])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'Ansari@123':
        return redirect(url_for('success', name = request.form['email']))
    return redirect(url_for('login'))
    
#trying flask templates with parameters

@app.route('/hi/<user>')
def hello_user(user):
    return render_template('hello.html',name = user)

@app.route('/result/<int:score>')
def result_display(score):
    return render_template('result.html',marks = score)

#trying tabular data feeding in Flask

















