FROM python:3.11

WORKDIR /code

COPY src/samdul12food/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/S00zzang/samdul12food@0.1.3

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
