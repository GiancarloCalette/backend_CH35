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

@app.get("/api/products/total")
def sum_prices():
    total = 0
    for product in mock_data:
        price = product["price"]
        total = total + price

    return json.dumps(total)

@app.get("/api/categories")
def categories():
    cats = []
    for product in mock_data:
        category = product["category"]
        if category not in cats:
            cats.append(category)
    return json.dumps(cats)

@app.get("/api/catalog/<category>")
def products_by_category(category):
    results = []
    for prod in mock_data:
        if prod["category"].lower() == category.lower():
            results.append(prod)
    return json.dumps(results)

@app.get("/api/products/lower/<price>")
def products_lower_price(price):
    fixed_price = float(price)
    results = []
    for prod in mock_data:
        if prod["price"] < fixed_price:
            results.append(prod)
    return json.dumps(results)

@app.get("/api/products/greater/<price>")
def products_greater_price(price):
    fixed_price = float(price)
    results = []
    for prod in mock_data:
        if prod["price"] >= fixed_price:
            results.append(prod)
    return json.dumps(results)

@app.get("/api/products/search/<term>")
def search_products(term):
    results = []
    for prod in mock_data:
        if term.lower() in prod["title"].lower():
            results.append(prod)
    return json.dumps(results)

app.run(debug=True)