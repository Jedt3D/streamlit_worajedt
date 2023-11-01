import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from st_pages import Page, show_pages

st.set_page_config(layout='wide')

# ----- Pages -----
show_pages(
    [
        Page('app.py', 'Home',''),
        Page('pages/tab.py', 'Layout',''),
        Page('pages/map.py', 'Map','')
    ]
)


st.markdown('สวัสดี! *Streamlit*')
st.title('Layout and Decoration')
st.write("""
 เราจะลองทำ San Francisco Dataset กันดู
""")
col1,col2,col3 = st.columns(3)
with col1:
   st.write('Column1')
with col2:
   st.write('Column2')
with col3:
   st.write('Column3')

tree_df = pd.read_csv('trees.csv')

df2 = pd.DataFrame(tree_df.groupby(['dbh']).count()['tree_id'])
df2.columns = ['tree_count']
st.line_chart(df2)
st.caption('กราฟแสดงจำนวนต้นไม้')
st.title('แปรผล')
print(df2)