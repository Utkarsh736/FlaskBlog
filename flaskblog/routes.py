from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Your acoount has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST']) # Login Form
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout") # Logout Form
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account") # Account route
@login_required
def account():
    return render_template('account.html', title='Account')