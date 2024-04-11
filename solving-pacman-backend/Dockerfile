FROM python:3.10-alpine
WORKDIR /backend
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root --no-directory
COPY solving_pacman_backend/ ./src
RUN poetry install --no-dev
EXPOSE 4000
WORKDIR /backend/src
CMD ["poetry", "run", "gunicorn", "-w", "4", "--bind", "0.0.0.0:4000", "wsgi:app" ]
