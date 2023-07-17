FROM python:3.10

ENV PYTHONUNBUFFERED=1
COPY scrapyd.conf /etc/scrapyd/
WORKDIR /app

RUN apt-get update && \
    apt-get install -y

COPY poetry.lock pyproject.toml ./

RUN pip install poetry hapless && \
    poetry config virtualenvs.in-project true && \
    poetry install
EXPOSE 6800
COPY . ./
CMD hap run poetry run scrapyd && sleep 5 && hap run poetry run scrapyd-deploy local && hap logs -f 1
