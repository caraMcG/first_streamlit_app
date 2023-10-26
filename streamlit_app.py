import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#setting fruit names to be index in select list
my_fruit_list = my_fruit_list.set_index('Fruit')

#select list to pick fruit user wants included
streamlit.multiselect("Pick some fruits:",  list(my_fruit_list.index), ['Avocado','Strawberries'])

#display table on page
streamlit.dataframe(my_fruit_list)
