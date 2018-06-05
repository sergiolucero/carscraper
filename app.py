from flask import Flask
from chilescraper import page_scrape

app = Flask(__name__)

@app.route("/scrape/<int:id>")
def hello(id):
    return page_scrape(id)