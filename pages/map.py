import streamlit as st
import pandas as pd
import numpy as np

def read_data():
   tree_df = pd.read_csv('../streamlit02/trees.csv')
   owners = st.sidebar.multiselect("Filter", tree_df['caretaker'].unique())
   st.sidebar.success("Select filter above.")
   query = '(index == index or index != index)'
   if owners != []:
       query += ' and caretaker in @owners'
   tree_df = tree_df.query(query)
   df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
   df_dbh_grouped.columns = ['tree_count']
   return df_dbh_grouped

df_dbh_grouped = read_data()

df_dbh_grouped1 = df_dbh_grouped.dropna()

df1 = pd.DataFrame(df_dbh_grouped1,columns=['latitude', 'longitude'])
st.map(df1)