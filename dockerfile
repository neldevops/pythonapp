FROM python:3.10.13-slim
WORKDIR /home/app
COPY requirements.txt /home/app/requirements.txt
RUN  pip install -r requirements.txt
COPY . .
CMD python3 app.py
