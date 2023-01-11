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
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

