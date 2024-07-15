FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV TOKEN=YOUR_TOKEN

CMD ["python", "./main.py"]
