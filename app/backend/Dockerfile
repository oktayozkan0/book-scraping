FROM python:3.10

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && \
    apt-get install -y

COPY poetry.lock pyproject.toml ./

RUN pip install poetry hapless && \
    poetry config virtualenvs.in-project true && \
    poetry install

EXPOSE 8000

COPY . ./
CMD poetry run uvicorn --host=0.0.0.0 main:app
