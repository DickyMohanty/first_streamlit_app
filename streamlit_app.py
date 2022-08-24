import streamlit

streamlit.title('I Love Biryani')

streamlit.header('Recipe')
streamlit.text('Rice')
streamlit.text('Meat')
streamlit.text('Masala')
streamlit.text('Onion')
streamlit.text('Ghee')
streamlit.text('Curd')


streamlit.header('Build Your Own Fruit Smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# pick the fruit
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
