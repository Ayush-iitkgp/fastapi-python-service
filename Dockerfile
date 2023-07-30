FROM python:3.10-buster

WORKDIR /opt/alpas-ai-solution

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip && \
    pip install "poetry==1.1.11" && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY src src

ENV PYTHONPATH /opt/alpas-ai-solution

CMD ["python", "src/main.py"]