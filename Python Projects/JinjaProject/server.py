from flask import Flask, render_template, jsonify
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    curYear = datetime.now().year
    return render_template("index.html", num = random_number, year = curYear)

@app.route('/guess/<name>')
def guess(name):
    api_url = f"https://api.agify.io?name={name}"
    response = requests.get(api_url)
    data = response.json()
    age = data["age"]
    return render_template("guess.html", name=name, age=age)

@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)