from flask import (
    Flask, 
    request,
    render_template
)

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")

@app.get("/users/new")
def create_user():
    return render_template("new_user.html")

@app.get("/users")
def user_list():
    return render_template("user_list.html")    
