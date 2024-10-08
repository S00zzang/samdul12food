from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime, timedelta
import csv
import os

import pymysql


app = FastAPI()

origins = [ "https://samdul12food.web.app/" ] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

#CSV 파일 경로
file_path = "/code/data/food.csv"

if not os.path.exists(file_path):
	os.makedirs(os.path.dirname(file_path), exist_ok=True)

@app.get("/")
def read_root():
	return{"hello": "n12"}

@app.get("/food")
def food(name: str):
	#kst = now + 9h
	kst_time = datetime.now() + timedelta(hours=9)
	#시간을 구함
	current_time = kst_time.strftime('%Y-%m-%d %H:%M:%S')
	#음식 이름과 시간을 csv 파일로 저장
	fields = ['food', 'time']
	data = {"food": name, "time": current_time}

	with open(file_path, 'a', newline='') as f:
		csv.DictWriter(f, fieldnames=fields).writerow(data)
	
	#DB 저장
	db = pymysql.connect(
		host = '172.17.0.1',
		port = 13306,
		user = 'food',
		passwd = '1234',
		db = 'fooddb',
		charset = 'utf8'
	)
	cursor = db.cursor(pymysql.cursors.DictCursor)

	sql = 'INSERT INTO foodhistory(username, foodname, dt) VALUES(%s, %s, %s)'
	cursor.execute(sql, ('n12', name, current_time))
	db.commit()

	return data
