import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from st_pages import Page, show_pages, add_page_title
import time

progress_text = "Loading. Please wait."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()
st.button("Reload")

# Defind
def read_data():
   tree_df = pd.read_csv('trees.csv')
   owners = st.sidebar.multiselect("Filter", tree_df['caretaker'].unique())
   st.sidebar.success("Select filter above.")
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

st.markdown('Hello everyone have a nice day!!! :balloon:')
st.title('Home')
st.write(""" Welcome to san francisco tree dataset """)
st.divider()

#---------------Create column-------------------------

df_dbh_grouped = read_data()
col1, col2, col3 = st.columns(3)
with col1:
    st.write('Column1')
    st.line_chart(df_dbh_grouped)
with col2:
    st.write('Column2')
    st.bar_chart(df_dbh_grouped)
with col3:
    st.write('Column3')
    st.area_chart(df_dbh_grouped)
st.divider()
