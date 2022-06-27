FROM python:3.9.5

WORKDIR /opt/app
ENV PYTHONPATH="."

RUN apt update -y

ADD . /opt/app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000/tcp

CMD ["python",  "api/app.py"]
