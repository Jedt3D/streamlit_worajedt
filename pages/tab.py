import streamlit as st
import pandas as pd
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