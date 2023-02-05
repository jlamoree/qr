FROM python:3.11
WORKDIR /app
RUN apt-get update && \
    apt-get install -y python3-zbar && \
    apt-get clean -y
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY decode.py /app
CMD ["python", "/app/decode.py"]
