from flask import Flask,render_template, url_for, flash,redirect
from forms import RegistrationForm, LogForm
import os


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


posts = [
    {
        'author' : 'Salah Youmir',
        'title' : 'Post 1',
        'content' : 'First post in the blog',
        'date_posted' : 'February the 6th 2020'
    },
    {
        'author' : 'Zayd Youmir',
        'title' : 'Post 2',
        'content' : 'Second post in the blog',
        'date_posted' : 'February the 18th 2020'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About blog')

@app.route('/register',methods =['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login',methods =['POST','GET'])
def login():
    form = LogForm()
    if form.validate_on_submit():
        if form.email.data == "s.youmir@gmail.com" and form.password.data == "password":
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful','danger')
        
    return render_template('login.html',title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)