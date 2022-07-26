FROM python:3.9-slim-buster

WORKDIR /flask-personal-portfolio

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000