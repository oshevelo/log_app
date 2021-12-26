FROM python:3.8-alpine
RUN apk update && apk upgrade && \
    apk add --update python3 && \
    apk add libpq-dev g++ \

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

RUN pip3 install django==3.2

COPY requirements.txt /usr/src/app/
RUN apk --no-cache add py3-pip python3-dev && \
    pip3 install -r requirements.txt && \
    apk del py3-pip python3-dev

RUN python3 manage.py collectstatic

COPY . /usr/src/app/

CMD ["/home/maxim1106/HillelProjects/log_app/env/bin/uwsgi uwsgi/production.ini"]