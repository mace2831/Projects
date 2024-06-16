import random

from flask import Flask
app = Flask(__name__)

correct_number = random.randint(0,9)

@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9</h1><iframe src="https://giphy.com/embed/3NtY188QaxDdC" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/3NtY188QaxDdC">via GIPHY</a></p>'

@app.route('/<int:guess>')
def one(guess):
    if guess == correct_number:
        return f'<h1>{guess} is the correct answer!</h1>'
    elif guess > correct_number:
        return f'<h1>{guess} is too high!</h1>'
    else:
        return f'<h1>{guess} is too low!</h1>'


if __name__ == "__main__":
    #run the app in debug mode
    app.run(debug=True)