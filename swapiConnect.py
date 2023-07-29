import streamlit as st
import requests
from streamlit.connections import ExperimentalBaseConnection


class SwapiConnect(ExperimentalBaseConnection[requests.Session]):
    """Basic st.experimental_connection implementation for API"""

    def _connect(self, **kwargs): # Create a connection session using requests
        if 'url' in kwargs:
           self.url = kwargs.pop('url')
        self.connection = requests.Session()
        return self.connection

    def cursor(self): #Return the connection as cursor
      if self.connection == None:
        return LookupError("Implement the Connection first")
      return self.connection

    @st.cache_data()
    def query(_self, query_param=None, url2=None):
        try:
            cursor = _self.cursor()
        except LookupError:
            return LookupError('Connection is not initalized')
        if url2:
            response = cursor.get(url2)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
               return None
        elif url2 == None:
          url = _self.url
          response = cursor.get(url+query_param)
          if response.status_code == 200:
              data = response.json()
              return data
          else:
              return None