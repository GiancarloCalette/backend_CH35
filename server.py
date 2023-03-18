from flask import Flask
import json
from about import me
from data import mock_data 

app = Flask(__name__)

############# WEB SERVER #################

@app.get("/")
def home():
    return "Hello world from a flask server"

@app.get("/test")
def test():
    return "This is a test page"

############# API SERVER #################
@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)

@app.get("/api/developer/name")
def dev_name():
    name = me["name"]
    last = me["last_name"]
    email = me["email"]
    response = f"{name} {last} -- {email}"
    return json.dumps(response)

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_data)

@app.get("/api/products/count")
def products_count():
    count = len(mock_data)
    return json.dumps(count)

app.run(debug=True)