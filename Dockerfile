FROM python:3.8.5
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN mkdir src
COPY requirements.txt /app/
RUN pip install -r requirements.txt && pip install -U pip
COPY src/ /app/src/