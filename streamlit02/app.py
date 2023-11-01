import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from st_pages import Page, show_pages

st.set_page_config(layout='wide')

# Create pages
show_pages(
    [
        Page('app.py', 'Home','🏠')
        # Page('pages/tab.py', 'Layout','📈'),
        # Page('pages/map.py', 'Map','🌍')
    ]
)


st.markdown('สวัสดี! *Streamlit*')
st.title('Layout and Decoration')
st.write("""
 เราจะลองทำ San Francisco Dataset กันดู
""")


# Read data & filter
tree_df = pd.read_csv('trees.csv')

owners = st.sidebar.multiselect("Owner filter", tree_df['caretaker'].unique())
query = '(index == index or index != index)'

if owners != []:
    query += ' and caretaker in @owners'

tree_df = tree_df.query(query)
df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
st.divider()

# ------ Columns ------
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