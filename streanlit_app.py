import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
try:
  #fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please enter a fruit to get information.')
  else:      
    #streamlit.write('The user entered ', fruit_choice)
    back_from_function = get_fruityvice_data(fruit_choice)
    # write out the normalised data in the form of a table
    streamlit.dataframe(back_from_function)
    
except URLError as e:
    streamlit.error()
#streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
#Snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
 
#Add a button to load the fruit
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)   
  
streamlit.header("View our fruit list. Add your favourite.")     
#allow the end user to add a fruit to the list
def insert_row_snowflake(add_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + add_fruit + "')")
    streamlit.text('Thanks for adding ' + add_fruit)
    
add_my_fruit = streamlit.text_input('Which fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  streamlit.text(back_from_function)
  
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")


