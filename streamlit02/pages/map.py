import streamlit as st
import pandas as pd
import numpy as np

# Read data & filter data
tree_df = pd.read_csv('trees.csv')
owners = st.sidebar.multiselect("Filter", tree_df['caretaker'].unique())
query = '(index == index or index != index)'
if owners != []:
    query += ' and caretaker in @owners'
tree_df = tree_df.query(query)

st.title('Map')
st.write(""" Welcome to san francisco tree dataset """)
st.divider()

tree_df1 = tree_df.replace('',np.nan)
tree_df1 = tree_df1.dropna(axis=0)
df1 = pd.DataFrame(tree_df1,columns=['latitude', 'longitude'])
st.map(df1)
