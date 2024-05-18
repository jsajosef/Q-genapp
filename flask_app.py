from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://localhost:8000/questions/')
    questions = response.json()
    return render_template('index.html', questions=questions)

if __name__ == "__main__":
    app.run(debug=True)