from flask import render_template,Flask,url_for,flash,redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Jackboy'
posts = [
    {
        'author': 'James',
        'title': 'John',
        'content': 'First post content',
        'date_posted': 'dated'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 'dates'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)