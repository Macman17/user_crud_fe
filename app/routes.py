
from urllib import response
from flask import (
    Flask, 
    request,
    render_template
)
import requests

app = Flask(__name__)
BACKEND_URL = 'http://127.0.0.1:5000/'

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/users/new")
def create_user():
    return render_template("new_user.html")
    
@app.get("/users/edit")
def user_edit():
    return render_template("user_edit.html")

@app.post("/users/create") 
def send_user_create_request():
    url = "%s/%s" % (BACKEND_URL, "users")
    form_data = request.form   
    user_json = {
        "first_name": form_data.get("first_name"),
        "last_name": form_data.get("last_name"),
        "hobbies": form_data.get("hobbies")
    }
    response = requests.post(url, json=user_json)
    if response.status_code == 204:
        return render_template("user_creation_success.html")                         
    else:
        return render_template("400.html"),400

@app.get("/users")
def user_list():
    url = "%s/%s" % (BACKEND_URL, "users")
    response = requests.get(url)
    if response.status_code == 200:
        resp_json= response.json()
        users=resp_json.get("users")
        return render_template("user_list.html", user_list=users) 
    else:
        return render_template("400.html"),400

@app.put("/users/<int:id>") 
def user_update(pk):
    url = "%s/%s" % (BACKEND_URL, pk['id'])
    form_data = request.form
    user_json = {
        "first_name": form_data.get("first_name"),
        "last_name": form_data.get("last_name"),
        "hobbies": form_data.get("hobbies")
        
    
    
    }
    response = requests.put(url, json=user_json)
    if response.status_code == 204:
        
        return render_template("user_updated.html")
    else:
        return render_template("400.html"),400