import streamlit as st
import pandas as pd
import numpy as np

tree_df = pd.read_csv('../streamlit02/trees.csv')
owners = st.sidebar.multiselect("Filter", tree_df['caretaker'].unique())
st.sidebar.success("Select filter above.")
query = '(index == index or index != index)'
if owners != []:
    query += ' and caretaker in @owners'
tree_df = tree_df.query(query)
# df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
# df_dbh_grouped.columns = ['tree_count']

tree_df1 = tree_df.replace('',np.nan)
tree_df1 = tree_df1.dropna(axis=0)
df1 = pd.DataFrame(tree_df1,columns=['latitude', 'longitude'])
st.map(df1)
