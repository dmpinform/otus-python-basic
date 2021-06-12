# To start the container run the command "docker run -p 5000:5000 web-app"
# Then follow the link "http://127.0.0.1:5000/"

FROM python:3.9.5-buster

WORKDIR /app

RUN pip install -U pip setuptools

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./web-app .

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]