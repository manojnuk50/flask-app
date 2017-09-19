FROM ubuntu:latest
MAINTAINER Manoj "manojkumar.vsj@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
RUN mkdir -p /usr/local/src/
COPY .db_config.yaml /usr/local/src/.db_config.yaml
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
