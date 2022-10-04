FROM python:3

ARG ENV

ENV ENV=${YOUR_ENV} \
    POETRY_VERSION=1.0.0

WORKDIR /app

RUN POETRY_VIRTUALENVS_CREATE=false pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml ./

RUN POETRY_VIRTUALENVS_CREATE=false poetry install $(test "ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY ./ddc .

CMD [ "bash", "start_app.sh" ]