FROM python:3.10-slim-buster

RUN apt update -y && apt install awscli -y

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]