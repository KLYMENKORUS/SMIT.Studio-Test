FROM python:3.10.6
RUN mkdir -p /src/

WORKDIR /src/

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONNUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . /src/
COPY init.json /src/