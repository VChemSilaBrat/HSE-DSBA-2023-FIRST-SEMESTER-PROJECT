# venv\scripts\activate
from flask import Flask, request, render_template, redirect, url_for
import plotly.express as px
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data_parsed.csv")
df["all_month"] = df["Year"] * 12  + df['Month']
# print(df)

@app.route('/about')
def home():
    return render_template("about.html")

@app.route('/')
def home_fix():
    return redirect(url_for('home'))

@app.route('/plots', methods=['GET', 'POST'])
def plots():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        start_month = int(start.split(".")[0])
        start_year = int(start.split(".")[1])
        end_month = int(end.split(".")[0])
        end_year = int(end.split(".")[1])
        gdf = df[(df["all_month"] >= start_month + start_year*12) & (df["all_month"] <= end_year * 12 + end_month)]
        # print(gdf)
        # print(start_month, start_year, end_month, end_year, sep = '\n')
        fig = px.line(
            gdf,
            x='datum',
            y=gdf.columns[1:-3],
            title='Your line graph'
        )
        fig_html = fig.to_html(full_html=False)
    try:
        return render_template("Plots.html", plot=fig_html)
    except UnboundLocalError:
        return render_template("Plots.html")
    else:
        return 'ВСЕ СЛОМАЛОСЬ, БЕГИТЕ!'

if __name__ == '__main__':
    app.run(port=8000, debug=False, host='0.0.0.0')
