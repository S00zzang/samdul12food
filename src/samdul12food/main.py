from typing import Union
from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
def read_root():
	return{"hello": "n12"}

@app.get("/food")
def food(name: str):
	#시간을 구함
	#음식 이름과 시간을 csv 파일로 저장 -> /code/data/food.csv
	#DB 저장
	print("=======================" + name)
	return{"food": name, "time": "2024-09-15 11:12:13"}
