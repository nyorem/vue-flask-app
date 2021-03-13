FROM python:3
EXPOSE 5000

WORKDIR /usr/src/app/backend
COPY backend .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./app.py"]
