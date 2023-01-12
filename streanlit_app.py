import streamlit
import pandas
import requests
streamlit.title('🥣 My parents new healthy diner 🥣')
streamlit.header('🍓🍅 Breakfast menu')
streamlit.text('🍇 Blueberry and Omega 3')
streamlit.text('🥤 Kale and spinach Rocket  smoothie')
streamlit.text('🍚 Hard boiled free range egg')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Banana','Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the list on the page
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# streamlit.text(fruityvice_response.json())
# get the json normalised form
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write out the normalised data in the form of a table
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector


