import streamlit
import pandas
streamlit.title('🥣 My parents new healthy diner 🥣')
streamlit.header('🍓🍅 Breakfast menu')
streamlit.text('🍇 Blueberry and Omega 3')
streamlit.text('🥤 Kale and spinach Rocket smoothie')
streamlit.text('🍚 Hard boiled free range egg')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
