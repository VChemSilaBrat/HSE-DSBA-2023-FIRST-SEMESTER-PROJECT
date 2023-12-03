# venv\scripts\activate
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/about')
def home():
    return render_template("About.html")

@app.route('/plots')
def plots():
    return render_template("Plots.html")

if __name__ == '__main__':
    app.run(port=8000, debug=True)
