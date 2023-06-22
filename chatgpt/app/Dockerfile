FROM python:3.11-rc-alpine

WORKDIR /app
COPY . .

RUN pip install poetry && \
    poetry install
    
CMD ["poetry", "run", "uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0", "--reload"]

EXPOSE 8000