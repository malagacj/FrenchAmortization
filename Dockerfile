FROM python:3.11-slim-bullseye

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000

CMD sleep 20 ;python manage.py runserver 0.0.0.0:8000
