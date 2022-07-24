import streamlit;
import panda;

streamlit.title('My Parents new Healthy Diner');
streamlit.header('Breakfast Menu');
streamlit.text('🥣 Omega 3 & Blueberry oat meal');
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie');
streamlit.text('🐔 Hard boiled Free-Range eggs');
streamlit.text('🥑🍞 Avacado Toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.dataframe(my_fruit_list);
