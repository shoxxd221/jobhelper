FROM python:3.10-alpine

WORKDIR /code

COPY ./req.txt /code/req.txt

RUN pip install --no-cache-dir --upgrade -r /code/req.txt

COPY ./app /code/app

ENV PYTHONPATH=/code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
