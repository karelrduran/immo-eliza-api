FROM python:3.11

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 --limit-max-requests 10000 --timeout-keep-alive 5 --log-level info
