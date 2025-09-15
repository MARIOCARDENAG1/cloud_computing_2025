from flask import Flask, request, redirect, render_template
from pymongo import MongoClient
import os 

app = Flask(__name__)
MONGO_HOST = os.getenv("MONGO_HOST", "db")
client = MongoClient(f"mongodb://{MONGO_HOST}:27017/")
db = client.notes_db
notes = db.notes

@app.route("/", methods=["GET"])
def home():
    return redirect("/create")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        note = {
            "email": request.form["email"],
            "text": request.form["text"],
            "tags": [t.strip() for t in request.form["tags"].split(",")]
        }
        notes.insert_one(note)
        return redirect(f"/user/{note['email']}")
    return render_template("create.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        tag = request.form["tag"].strip()
        results = list(notes.find({"tags": tag}))
    return render_template("search.html", results=results)

@app.route("/user/<email>")
def user_notes(email):
    results = list(notes.find({"email": email}))
    return render_template("user.html", results=results, email=email)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
