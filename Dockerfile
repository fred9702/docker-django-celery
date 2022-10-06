FROM python:3

WORKDIR /app

RUN POETRY_VIRTUALENVS_CREATE=false pip install poetry

COPY poetry.lock pyproject.toml ./

RUN POETRY_VIRTUALENVS_CREATE=false poetry install

COPY ./ddc .

CMD [ "bash", "start_app.sh" ]