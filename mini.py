# -*- coding:utf-8 -*-
import pandas as pd 
import streamlit as st 
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data_aisles():
    df = pd.read_csv(r'total_data\new_orders.csv')
    return df

def main():
    st.title("Instacart Market Basket Analysis 과제 연습")

    # Load data
    df = load_data_aisles()

    # Display first few rows of the dataframe
    st.subheader("샘플 데이터")
    st.dataframe(df.head())

    # Display basic statistics of the dataframe
    st.subheader("데이터 요약")
    st.write(df.describe())

    # Visualize order distribution by day of week
    st.subheader("일주일 중 어떤 날에 주문을 했나")
    #'''plt.figure(figsize=(10, 6))
    #sns.countplot(x='order_dow', data=df)
    #plt.xlabel("Day of Week")
    #plt.ylabel("Order Count")
    #st.pyplot()'''
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.countplot(x='order_dow', data=df, ax=ax1)
    plt.xlabel("Day of Week")
    plt.ylabel("Order Count")
    st.pyplot(fig1)
    st.write('-'*100)

    # Visualize order distribution by hour of day
    st.subheader("하루 중 몇 시에 주문을 했는지")
    #'''plt.figure(figsize=(10, 6))
    #sns.countplot(x='order_hour_of_day', data=df)
    #plt.xlabel("Hour of Day")
    #plt.ylabel("Order Count")
    #st.pyplot()'''
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.countplot(x='order_hour_of_day', data=df, ax=ax2)
    plt.xlabel("Hour of Day")
    plt.ylabel("Order Count")
    st.pyplot(fig2)
    st.write('-'*100)

    # Visualize days since prior order distribution
    st.subheader("이전 주문으로부터 몇 일 뒤에 주문을 했는지")
    #'''plt.figure(figsize=(10, 6))
    #sns.histplot(df['days_since_prior_order'].dropna(), bins=20, kde=True)
    #plt.xlabel("Days Since Prior Order")
    #plt.ylabel("Frequency")'''
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.histplot(df['days_since_prior_order'].dropna(), bins=20, kde=True, ax=ax3)
    plt.xlabel("Days Since Prior Order")
    plt.ylabel("Order Count")
    st.pyplot(fig3)

if __name__ == "__main__":
    main()