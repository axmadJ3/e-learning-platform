FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY req.txt ./

RUN pip install --no-cache-dir -r req.txt

COPY . .

WORKDIR /app/educa

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
    