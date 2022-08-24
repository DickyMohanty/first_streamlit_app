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
my_fruit_list = my_fruit_list.set_index('Fruit')


# pick the fruit
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

# display the table on the page
streamlit.dataframe(my_fruit_list)

# pick fruit they want to include
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado', 'Strawberries'])

# pick fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display table on the page
streamlit.dataframe(fruits_to_show)
