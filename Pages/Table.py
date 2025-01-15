import streamlit as st
import pandas as pd

st.title("Table View")

apps = st.selectbox("Select a Table",["Customers","Restaurants","Orders","Deliveries"])

if apps == "Customers":
    data = pd.read_csv("C:/Users/ADMIN/Zomato Data Insights/Datasets/Customers.csv")
    st.dataframe(data)
elif apps == "Restaurants":
    data = pd.read_csv("C:/Users/ADMIN/Zomato Data Insights/Datasets/Restaurants.csv")
    st.dataframe(data)
elif apps == "Orders":
    data = pd.read_csv("C:/Users/ADMIN/Zomato Data Insights/Datasets/Orders.csv")
    st.dataframe(data)
elif apps == "Deliveries":
    data = pd.read_csv("C:/Users/ADMIN/Zomato Data Insights/Datasets/Deliveries.csv")
    st.dataframe(data)