import streamlit as st
from swapiConnect import SwapiConnect


def main():
  st.header("Star Wars API")
  st.image('starwars.png')

  # setup the connection
  connection = st.experimental_connection('swapi', type=SwapiConnect)
  connection._connect(url="https://swapi.dev/api/") #Initialize the connection

  titles = []
  characters = []
  for i in range(1, 7):
    # Use the query method to retrieve data
    data = connection.query(f'films/{i}')
    titles.append(data['title'])

  option = st.selectbox('Choose a movie', titles)
  movie_num = int(titles.index(option)) + 1
  movie_data = connection.query(f"/films/"+str(movie_num))
  characters_data = movie_data["characters"]
  for char in characters_data:
     character = connection.query(url2=char)
     characters.append(character['name'])

  st.write("Title : ", option)
  st.write("Director : ", movie_data['director'])
  st.write("Release Date : ", movie_data['release_date'])
  st.subheader("Characters")
  for i in characters:
     st.write(i)

  st.subheader("Opening Crawl")
  st.text(movie_data['opening_crawl'])

  st.divider()

  st.text('''This app is built to showcase the new feature i.e. st.ExperimentalBaseConnection
           and used swapi.dev which is an starwars api.''')

if __name__ == "__main__":
    main()