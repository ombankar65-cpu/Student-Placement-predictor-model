FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Flask apps must bind to 0.0.0.0
ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["python", "app.py"]
