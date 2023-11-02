import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from st_pages import Page, show_pages, add_page_title
import time

#---------------Create page-------------------------
#st.set_page_config(layout='wide')
add_page_title()

show_pages([
        Page('app.py', 'Home','🏠'),
        Page('tab.py', 'Tab','📈')
        # Page('pages/map.py', 'Map','🌍')
          ])

st.markdown('สวัสดี! *Streamlit*')
st.title('Layout and Decoration')
st.write("""
 เราจะลองทำ San Francisco Dataset กันดู
""")
st.divider()

with st.spinner('Loading...'):
    time.sleep(5)
# st.success('Done!')

#---------------Read data & filter-------------------------
tree_df = pd.read_csv('trees.csv')

owners = st.sidebar.multiselect("Owner filter", tree_df['caretaker'].unique())
st.sidebar.success("Select filter above.")
query = '(index == index or index != index)'

if owners != []:
    query += ' and caretaker in @owners'

tree_df = tree_df.query(query)
df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

#---------------Create column-------------------------

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