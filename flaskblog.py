from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# __name__ is name of module (spl. var. in python)

app = Flask(__name__)

app.config['SECRET_KEY'] = '4d02ba5bcbaee679dd80e78cba5644b7'


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


@app.route("/register", methods=['GET', 'POST']) # Registration Form
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login") # Login Form
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
