import pandas as pd
import streamlit as st

df=pd.read_csv('C:/Users/ASUS/.vscode/lib.pr.py/data/raw/Adata.csv')
st.dataframe(df)


sales_by_city=df.groupby("city")["total_sales"].sum()






st.title("Sales Analysis")

name=st.text_input("Enter your name")
Age =st.number_input("Enter your age: ")
gender=st.radio("Gender : ",["male","female"])
food=st.multiselect("fev food : ",["bread","chabati","butter","Burger"])

st.subheader("Sales by City")
st.bar_chart(sales_by_city,color="red",)
columns=df.columns
select_column=st.selectbox("Select a column",columns)

st.subheader(f"Sales by {select_column}")
sales_by_paymentmethod=df.groupby(select_column)["total_sales"].sum()
st.bar_chart(sales_by_paymentmethod,width=500,height=500,color="green")








