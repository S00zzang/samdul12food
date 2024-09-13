from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from datetime import datetime
import csv
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8899/","https://samdul12food.web.app/"],  # 허용할 출처 (클라이언트 URL)
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

#CSV 파일 경로
CSV_FILE_PATH = '/code/samdul12food/food.csv'

@app.get("/")
def read_root():
	return{"hello": "n12"}

@app.get("/food")
def food(name: str):
	#시간을 구함
	current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	#음식 이름과 시간을 csv 파일로 저장 -> /code/samdul12food/food.csv
	file_exists = os.path.isfile(CSV_FILE_PATH)

	with open(CSV_FILE_PATH, mode='a', newline='', encoding='utf-8') as file:
		writer = csv.writer(file)
		if not file_exists:
			writer.writerow(['Timestamp'], ['Food Name'])
		writer.writerow([current_time, name])
	
	#DB 저장
	print("=======================" + name)
	return{"food": name, "time": current_time}
