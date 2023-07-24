import streamlit as st
import requests
from streamlit.connections import ExperimentalBaseConnection


class SwapiConnect(ExperimentalBaseConnection):

    def __init__(self, url):
        super().__init__("swapi")
        self.url = url

    def _connect(self): # Create a connection session using requests
        self.connection = requests.Session()

    def cursor(self): #Return the connection as cursor
      if self.connection == None:
        self._connect()
      return self.connection

    @st.cache_data(ttl=60 * 60)
    def query(_self, query_param=None, url2=None):
        if url2:
            response = _self.connection.get(url2)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
               return None
        elif url2 == None:
          url = _self.url
          response = _self.connection.get(url+query_param)
          if response.status_code == 200:
              data = response.json()
              return data
          else:
              return None