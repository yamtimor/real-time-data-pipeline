FROM bitnami/spark:latest 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY . . 
CMD ["spark-submit", "consumer.py"] 
