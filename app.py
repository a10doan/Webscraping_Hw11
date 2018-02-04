# Dependencies
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create a Flask app
app = Flask(__name__)

# Connect to MongoDB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Use database and create it if it does not exist
db = client.martiansDB
  

# Create index route
@app.route("/")
def index():

    mars_data = db.mars_collection.find_one()

    # Render html
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
    scraped_data = scrape_mars.scrape()
    db.mars_collection.update(
        {},
        scraped_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)