# -*- coding: utf-8 -*-
"""tp_redes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nrSkq1winbyCatb_xCblYdj4HD77TVlE
"""

from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import json
import pandas as pd
app = FastAPI()
#@app.get("/get-pelis")
#def get_pelis():
#    url ='https://gitlab.com/julietatexier93/redes_de_datos/-/raw/main/peliculas_disney.json'
#    pelis = pd.read_json(url)
#    return pelis


with open('peliculas_disney.json') as file:
  data = json.load(file)

  class Item(BaseModel):
    title: str
    description: str


  @app.get("/")
  def read_root():
      return {"Hello": "World"}

  @app.get("/get-pelis")
  def get_pelis():
      url ='https://gitlab.com/julietatexier93/redes_de_datos/-/raw/main/peliculas_disney.json'
      pelis = pd.read_json(url)
      return pelis

  @app.get("/titulo/{item_id}")
  def read_item(item_id: int):
      return data['movies'][item_id]["title"]
    #el problema es que no logra encontrar el item_id, pero si le pedimos que retorne un numero en particular (por ejemplo un 1 en donde dice return) lo devuelve

  #@app.get("/peli-mas-larga")
  
  #@app.get("/peli-mas-nueva")



#  @app.put("/peli-nueva/{item_id}")
#  def update_item(item_id: int, item: Item):
#    return 
