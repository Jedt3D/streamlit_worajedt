import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("Iris")
st.title("Iris Dataset")
st.markdown('สร้าง `scatter plot` แสดงผลข้อมูล **Iris dataset**')

choices = ['sepal.length','sepal.width','petal.length','petal.width']
iris_file = None
iris_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)

if iris_file is not None:
    iris_df = pd.read_csv(iris_file)
else:
    st.stop()

st.subheader('ข้อมูลตัวอย่าง')
st.write(iris_df.head(5))

selected_x_var = st.selectbox('What do you want to select x?',(choices))
selected_y_var = st.selectbox('What do you want to select y?',(choices))

st.subheader('แสดงผลข้อมูล')
sns.set_style('darkgrid')
markers = {"Setosa": "v", "Virginica": "s", "Versicolor": 'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data=iris_df,
                     x=selected_x_var, y=selected_y_var,
                     hue='variety', markers=markers, style='variety')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("iris Data")
st.pyplot(fig)

st.title('iris Classifier')
st.write("This app uses 4 inputs to predict the variety of iris")

iris_df = iris_df.dropna()

output = iris_df['variety']
features = iris_df[['sepal.length', 'sepal.width', 'petal.length','petal.width']]

features = pd.get_dummies(features)

output, unique_iris_mapping = pd.factorize(output)

x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=.8)

rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train, y_train)

y_pred = rfc.predict(x_test)

score = round(accuracy_score(y_pred, y_test), 2)

st.write('We trained a Random Forest model on these data,'
             ' it has a score of {}! Use the '
             'inputs below to try out the model.'.format(score))


with st.form('user_inputs'):
    sepal_length = st.number_input('sepal.length', min_value=0.0,max_value=10.0, value=0.0)
    sepal_width  = st.number_input('sepal.width' , min_value=0.0,max_value=10.0, value=0.0)
    petal_length = st.number_input('petal.length', min_value=0.0,max_value=10.0, value=0.0)
    petal_width  = st.number_input('petal.width' , min_value=0.0,max_value=5.0, value=0.0)
    st.form_submit_button()

new_prediction = rfc.predict([[sepal_length, sepal_width, petal_length,petal_width]])

prediction_species = unique_iris_mapping[new_prediction][0]

st.write('We predict variety is the {}'.format(prediction_species))

