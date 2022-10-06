FROM python:3

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install

COPY /ddc /app/

ENTRYPOINT [ "bash", "start_app.sh" ]