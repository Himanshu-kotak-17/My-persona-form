FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt update -y

RUN apt install sqlite3

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3","app.py" ]
