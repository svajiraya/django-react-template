FROM python:3
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD ./ /backend
WORKDIR /backend

EXPOSE 8000
