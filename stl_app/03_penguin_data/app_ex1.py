import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Palmer's Penguins")
st.markdown('สร้าง `scatter plot` แสดงผลข้อมูล **Palmer\'s Penguins** กัน แบบเดียวกับ **Iris dataset**')

choices = ['bill_length_mm',
           'bill_depth_mm',
           'flipper_length_mm',
           'body_mass_g']


selected_x_var = st.selectbox('เลือกตัวแปรแกน x', choices)
selected_y_var = st.selectbox('เลือกตัวแปรแกน y', choices)

penguin_file = st.file_uploader('เลือกไฟล์ Penguins CSV แล้ว Upload', type=['csv'])

if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()

st.subheader('ข้อมูลตัวอย่าง')
st.write(penguins_df)

st.subheader('แสดงผลข้อมูล')
sns.set_style('darkgrid')
markers = {"Adelie": "v", "Gentoo": "s", "Chinstrap": 'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data=penguins_df,
                     x=selected_x_var, y=selected_y_var,
                     hue='species', markers=markers, style='species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Palmer's Penguins Data")
st.pyplot(fig)
