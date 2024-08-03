FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get upgrade
RUN pip install --upgrade pip

COPY requirements.txt .
COPY . /app

RUN pip install -r requirements.txt

CMD ["fastapi", "run", "main.py"]
