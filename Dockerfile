FROM python:3.8-slim-buster

# Install libgomp1
RUN apt-get update && apt-get install -y libgomp1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY codes/ /app/codes/
COPY models/ /app/models/

EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["codes.main:app", "--host", "0.0.0.0", "--port", "8000"]
