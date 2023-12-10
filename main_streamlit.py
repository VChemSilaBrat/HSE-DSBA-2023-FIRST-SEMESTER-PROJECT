# python -m venv venv
# cd C:\Users\psard\projects\HSE-DSBA-2023-FIRST-SEMESTER-PROJECT
# venv\scripts\activate
# pip install -r requirements.txt
# streamlit run main_streamlit.py
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

df = pd.read_csv("data_parsed.csv", parse_dates=["datum"])

if __name__ == "__main__":
    st.set_page_config(
        page_title="Drug sales data",
        page_icon="💊",
        initial_sidebar_state="collapsed",
        layout="wide",
    )
    with st.sidebar:
        st.write("Project info")
        st.link_button("Data link", "https://www.kaggle.com/datasets/milanzdravkovic/pharma-sales-data/data?select=salesmonthly.csv")
        st.image("memes.jpg")
        st.write("Sardak Pavel, 2023, GPL3.")
    st.header("Drugs sales dataset")
    st.subheader("Parsed data")
    st.dataframe(df, use_container_width=True)
    st.subheader("Data describe")
    st.dataframe(df.describe(include=[np.number]), use_container_width=True)
    st.subheader("Here are interactive line graph")
    year_list = ['All years'] + list(df['Year'].unique())
    # print(list(year_list) + ['all'])
    year = st.selectbox("Select a year to show :blue[line graph]", year_list)
    if year != 'All years':
        gdf = df[df["Year"] == year]
        line_chart = px.line(
            gdf,
            x="datum",
            y = df.columns[:-2],
            title=f"Sales in {year} per month in compare",
        )
        st.plotly_chart(line_chart, use_container_width=True)
    else:
        line_chart = px.line(
            df,
            x="datum",
            y = df.columns[:-2],
            title=f"Sales in {year.lower()} per month in compare",
        )
        st.plotly_chart(line_chart, use_container_width=True)
    show_code = st.checkbox("Show code?")
    if show_code:
        st.subheader("Code")
        st.code("""year = st.selectbox("Select a year to show :blue[line graph]", year_list)
    if year != 'All years':
        gdf = df[df["Year"] == year]
        line_chart = px.line(
            gdf,
            x="datum",
            y = df.columns[:-2],
            title=f"Sales in {year} per month in compare",
        )
        st.plotly_chart(line_chart, use_container_width=True)
    else:
        line_chart = px.line(
            df,
            x="datum",
            y = df.columns[:-2],
            title=f"Sales in {year.lower()} per month in compare",
        )
        st.plotly_chart(line_chart, use_container_width=True)""")
    year = st.selectbox("Select a year to show :blue[pie chart]", year_list)
    if year != 'All years':
        gdf = df[df["Year"] == year]
        gdf = gdf[gdf.columns[1:-2]]
        pie_chart = px.pie(
            gdf,
            values=gdf.sum(),
            names=gdf.columns,
            title=f"Sales in {year} per month in compare",
            hole=0.3,
        ).update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(pie_chart, use_container_width=True)
    else:
        pie_chart = px.pie(
            df,
            values=df[df.columns[1:-2]].sum(),
            names=df.columns[1:-2],
            title=f"Sales in {year.lower()} per month in compare",
            hole=0.3,
        ).update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(pie_chart, use_container_width=True)
    show_code_1 = st.checkbox("Show code? ")
    if show_code_1:
        st.subheader("Code")
        st.code("""year = st.selectbox("Select a year to show :blue[pie chart]", year_list)
    if year != 'All years':
        gdf = df[df["Year"] == year]
        gdf = gdf[gdf.columns[1:-2]]
        pie_chart = px.pie(
            gdf,
            values=gdf.sum(),
            names=gdf.columns,
            title=f"Sales in {year} per month in compare",
            hole=0.3,
        ).update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(pie_chart, use_container_width=True)
    else:
        pie_chart = px.pie(
            df,
            values=df[df.columns[1:-2]].sum(),
            names=df.columns[1:-2],
            title=f"Sales in {year.lower()} per month in compare",
            hole=0.3,
        ).update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(pie_chart, use_container_width=True)""")