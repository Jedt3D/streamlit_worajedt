import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from st_pages import Page, show_pages, add_page_title
import time

# #---------------Create page-------------------------
#
#
# show_pages([
#         Page('app.py', 'Home','🏠'),
#         Page('tab.py', 'Tab','📈')
#         # Page('pages/map.py', 'Map','🌍')
#           ])
#
# st.markdown('สวัสดี! *Streamlit*')
# st.title('Layout and Decoration')
# st.write("""
#  เราจะลองทำ San Francisco Dataset กันดู
# """)
#
#
#
# #---------------Read data & filter-------------------------
# tree_df = pd.read_csv('trees.csv')
# owners = st.sidebar.multiselect("Owner filter", tree_df['caretaker'].unique())
# st.sidebar.success("Select filter above.")
#
# query = '(index == index or index != index)'
# if owners != []:
#     query += ' and caretaker in @owners'
#
# tree_df = tree_df.query(query)
# df_dbh_grouped = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
# df_dbh_grouped.columns = ['tree_count']
#
# #---------------Create column-------------------------
#
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.write('Column1')
#     st.line_chart(df_dbh_grouped)
# with col2:
#     st.write('Column2')
#     st.bar_chart(df_dbh_grouped)
# with col3:
#     st.write('Column3')
#     st.area_chart(df_dbh_grouped)
# st.divider()

# Read data & filter
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


# Define the pages
def home_page():
   st.markdown(f"# {list(pages.keys())[0]}")
   st.title('San Francisco dataset')
   st.write(""" Let's go """)

   df_dbh_grouped = read_data()

   # Create column
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

def tab_page():
   st.markdown(f"# {list(pages.keys())[1]}")
   st.title('San Francisco dataset')
   st.write(""" Let's go """)

   df_dbh_grouped = read_data()

   # Create tab
   tab1, tab2, tab3 = st.tabs(["Line", "Bar", "Area"])
   with tab1:
       st.write('Column1')
       st.line_chart(df_dbh_grouped)
   with tab2:
       st.write('Column2')
       st.bar_chart(df_dbh_grouped)
   with tab3:
       st.write('Column3')
       st.area_chart(df_dbh_grouped)


def map_page():
   st.markdown(f"# {list(pages.keys())[2]}")
   st.title('San Francisco dataset')
   st.write(""" Let's go """)


# Create a dictionary of pages
pages = {
   "Home": home_page,
   "Tab": tab_page,
   "Map": map_page
}
# Add a selectbox to the sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Go to", list(pages.keys()))
# Display the selected page
page = pages[selection]
page()

