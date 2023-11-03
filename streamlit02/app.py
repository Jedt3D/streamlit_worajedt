import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from st_pages import Page, show_pages, add_page_title

# Defind
def filter_data(tree_df):
   owners = st.sidebar.multiselect("Owner Filter", tree_df['caretaker'].unique())
   query = '(index == index or index != index)'
   if owners != []:
       query += ' and caretaker in @owners'
   tree_df = tree_df.query(query)
   df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
   df_dbh_grouped.columns = ['tree_count']
   return df_dbh_grouped

#---------------Create page-------------------------
show_pages([
        Page('app.py', 'Home','🏠'),
        Page('../pages/tab.py', 'Tab', '📈'),
        Page('../pages/map.py', 'Map', '🌍')
          ])
st.title('Home')
st.write(""" Welcome to san francisco tree dataset """)
st.divider()

# Read data
tree_df = pd.read_csv('trees.csv')

#---------------Create column-------------------------
result = filter_data(tree_df)
col1, col2, col3 = st.columns(3)
with col1:
    st.write('Column1')
    st.line_chart(result)
with col2:
    st.write('Column2')
    st.bar_chart(result)
with col3:
    st.write('Column3')
    st.area_chart(result)
st.divider()
