FROM python:3.10-buster

WORKDIR /opt/alpas-ai-solution

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip && \
    pip install "poetry==1.1.11" && \
    poetry config virtualenvs.create false && \
    poetry install

COPY src src

COPY scripts scripts

COPY tests tests

ENV PYTHONPATH /opt/alpas-ai-solution

CMD ["python", "src/bin/api.py"]