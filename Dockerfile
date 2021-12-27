FROM python:3.9-alpine

RUN apk update && apk upgrade
RUN apk add python3-dev g++ libpq-dev libffi-dev zlib-dev jpeg-dev
RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /log_app
COPY . /log_app
WORKDIR /log_app
RUN python3 -m pip install -r requirements.txt

CMD ["uwsgi", "--ini", "/log_app/uwsgi/logapp_uwsgi.ini"]
