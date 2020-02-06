from flask import Flask,render_template


app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)