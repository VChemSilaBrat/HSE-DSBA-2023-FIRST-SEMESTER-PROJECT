# venv\scripts\activate
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Это главная страница.'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
