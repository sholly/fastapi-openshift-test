FROM python:alpine

USER root
COPY requirements.txt / 
RUN apk add build-base && \
    pip install -r /requirements.txt

COPY main.py / 
USER 1001
EXPOSE 8080
CMD python3 /main.py
