import streamlit as st
import pandas as pd

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

st.title('Tab')
st.write(""" Welcome to san francisco tree dataset """)
st.divider()

# Read data
tree_df = pd.read_csv('trees.csv')

#---------------Create tab-------------------------
result = filter_data(tree_df)
tab1, tab2, tab3 = st.tabs(["Line", "Bar", "Area"])
with tab1:
    st.write('Column1')
    st.line_chart(result)
with tab2:
    st.write('Column2')
    st.bar_chart(result)
with tab3:
    st.write('Column3')
    st.area_chart(result)