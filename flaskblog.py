from flask import Flask

# __name__ is name of module (spl. var. in python)

app = Flask(__name__)

# Creating routes for differnet pages
# Using Decorators

@app.route("/") # Home page
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about") # About page
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
