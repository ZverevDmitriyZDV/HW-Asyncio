
FROM python:3.9.9-alpine3.14

ARG DB

ENV DB=$DB

WORKDIR /code

COPY . /code

RUN apk add --no-cache --virtual .build-deps g++ gcc make libc-dev libffi-dev libevent-dev musl-dev \
    openssl-dev \
    && pip install --no-cache-dir -r /code/requirements.txt \
    && apk del .build-deps g++ gcc make libc-dev libffi-dev libevent-dev musl-dev openssl-dev

ENTRYPOINT ./entrypoint.sh