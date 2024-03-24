import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import plotly as px
import seaborn as sns

st.title("Iris Data Set")
st.subheader("Welcome to Iris Data Explorer")

def load_irisdata():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    dtf=pd.read_csv(url, header=None, names=column_names)
    return dtf

data=load_irisdata()

#Data Displaying
if st.checkbox("Show Raw Data"):
   st.subheader("Raw Data")
   st.dataframe(data)

#Average Sepal Length
if st.checkbox("Show the average sepal length for each species"):
    st.subheader("Average Sepal Length for Each Species")
    avg_sepal_length = data.groupby("species")["sepal_length"].mean()
    st.write(avg_sepal_length)

#Scarter Plot Q2
st.subheader("Scatter Plot Comparison")
item_1 = st.selectbox("Select the first feature:", data.columns[:-1])
item_2 = st.selectbox("Select the second feature:", data.columns[:-1])


import plotly
print(plotly.__version__)
import plotly.express as px
scatter_plot = px.scatter(data, x=item_1, y=item_2, color="species", hover_name="species")
st.plotly_chart(scatter_plot)

#Filtered Data
st.subheader("Filtered Species")
selected_species = st.multiselect("Select species to display:", data["species"].unique())

if selected_species:
    filtered_data = data[data["species"].isin(selected_species)]
    st.dataframe(filtered_data)
else:
    st.write("No Species Has Been Selected.")

#Pairplot for the selected species
st.subheader("Pairplot")
if st.checkbox("Show pairplot for selected Species"):
    st.subheader("Pairplot for the Selected Species")

    if selected_species:
        sns.pairplot(filtered_data, hue="species")
    else:
        sns.pairplot(data, hue="species")
        
    st.pyplot()

#Distribution of a Selected featureS
st.subheader("Distribution of a Selected Feature")
selected_feature = st.selectbox("Select a feature to display its distribution:", data.columns[:-1])


import plotly
print(plotly.__version__)
import plotly.express as px
histo= px.histogram(data, x=selected_feature, color="species", nbins=30, marginal="box", hover_data=data.columns)
st.plotly_chart(histo)

st.subheader("Thank You, Hope you enjoyed exploring Iris Data")
st.balloons()