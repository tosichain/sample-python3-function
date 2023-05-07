FROM python:3.11.3-alpine3.17

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

COPY ./init /init

RUN chmod +x /init

ENTRYPOINT ["python", "src/main.py"]
