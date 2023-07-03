FROM python:3.9 AS builder

# the secret is only used to sign runtime parameter payloads, so there is no need to keep it "secret".
ARG PYTM_SECRET=43b4d4de-162c-4223-89ea-713a76a1ec63

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim

LABEL pytm.version="1.0.0"

ENV PYTM_SECRET=${PYTM_SECRET}

EXPOSE 8080

WORKDIR /usr/src/app

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

RUN pip install --no-cache-dir gunicorn

RUN useradd -ms /bin/sh user

WORKDIR /home/user

COPY . .

USER user

CMD gunicorn -b 0.0.0.0:8080 app:app
