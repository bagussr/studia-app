FROM tiangolo/uvicorn-gunicorn:python3.10 as base

COPY ./app /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENV PORT=8080