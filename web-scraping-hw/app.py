from scraped import pyscript
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")

@app.route("/")
def welcome():
    mars_d = mongo.db.mars.find_one()
    return (render_template("index.html", m=mars_d))


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = pyscript()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == '__main__':
    app.run()