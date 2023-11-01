mport streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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