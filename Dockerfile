FROM fnndsc/python-poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root