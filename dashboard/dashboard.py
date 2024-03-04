import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from tabulate import tabulate
import plotly.express as px

sns.set(style='dark')


st.write("""
    # Data Analysis of E-Commerce in Brazil
    The data analysis focuses on the top 10 products with the highest sales in Brazil and the most commonly used payment types for each state in Brazil.
""")

prod_df = pd.DataFrame({
    'product_category_name': ["cama_mesa_banho", "esporte_lazer", "moveis_decoracao", "beleza_saude", "utilidades_domesticas", "automotivo", "informatica_acessorios", "brinquedos", "relogios_presentes", "telefonia"],
    'product_count': [3029, 2867, 2657, 2444, 2335, 1900, 1639, 1411, 1329, 1134]
})

st.title('Top 10 best-selling products in Brazilian E-Commerce')
st.bar_chart(prod_df.set_index('product_category_name')['product_count'])


with st.expander("Explanation"):
    st.write("Based on the analysis results, it can be observed that the product category with the highest sales is 'cama_mensa_banho' accounting for 3029 products.")



#============================
st.title('Top 10 Product Categories Proportions')

col1, col2 = st.columns(2)

with col1:
    st.table(prod_df)

with col2:
    category_proportions = prod_df['product_count'] / prod_df['product_count'].sum()

    fig = px.pie(prod_df, values='product_count', names='product_category_name', 
        title='Proportion of Products in Each Category',
        labels={'product_category_name': 'Category'},
        template='plotly')

    st.plotly_chart(fig)

with st.expander("Explanation"):
    st.write("Based on the analysis results, the highest percentage among the top 10 best-selling products is cama_mesa_banho, amounting to 14.6%.")

#============================================

df = pd.read_csv('dashboard/geocustomer.csv')
state_payment_counts = df.groupby(['customer_state', 'payment_type']).size().reset_index(name='count')
st.title('Payment Types by State')
fig = px.bar(state_payment_counts, 
             x='customer_state', 
             y='count', 
             color='payment_type',
             labels={'count': 'Count', 'customer_state': 'Customer State'},
             title='Payment Types by State',
             barmode='group')
st.plotly_chart(fig)

with st.expander("Explanation"):
    st.write("Based on the analysis results, it can be observed that the majority of the population or customers in all states in Brazil prefer to shop using credit card payments compared to other payment types. The highest number of users is found in the state of São Paulo.")


st.title('Payment Types by State Detail')
selected_state = st.selectbox('Choose State:', df['customer_state'].unique())
filtered_df = df[df['customer_state'] == selected_state]
payment_counts = filtered_df['payment_type'].value_counts()
st.write(f"Most Frequently Used Payment Types in {selected_state}:")
st.table(payment_counts)
st.bar_chart(payment_counts)
