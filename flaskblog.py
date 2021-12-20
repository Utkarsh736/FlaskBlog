from flask import Flask, render_template, url_for

# __name__ is name of module (spl. var. in python)

app = Flask(__name__)

posts = [
    {
        'author': 'Utkarsh Tomar',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 20, 2021'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 21, 2021'
    }
]

# Creating routes for differnet pages
# Using Decorators

@app.route("/") # Home page
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about") # About page
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
