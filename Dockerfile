FROM python:3.8-alpine
RUN apk update && apk upgrade && \
    apk add --update python3 && \
    apk add libpq-dev g++ \

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN apk --no-cache add py3-pip python3-dev && \
    pip3 install -r requirements.txt && \
    apk del py3-pip python3-dev

RUN python3 manage.py collectstatic

COPY . /usr/src/app/

CMD ["/home/max/HillelProjects/log_app/venv/bin/uwsgi uwsgi/production.ini"]