# ------------------------------------------------------------
# Build Container --------------------------------------------
# ------------------------------------------------------------
FROM python:3.9-slim as builder

WORKDIR /opt/app

RUN python3 -m pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt > requirements.txt

# ------------------------------------------------------------
# Runtime Container ------------------------------------------
# ------------------------------------------------------------
FROM python:3.9-slim as runtime

WORKDIR /opt/app

ENV PYTHONBUFFERED=1
COPY --from=builder /opt/app/requirements.txt .
RUN python3 -m pip install -U setuptools pip && \
    python3 -m pip install -r requirements.txt

# COPY . .

EXPOSE 8000
CMD [ "uvicorn", "ifconfig.app:app", "--host", "0.0.0.0" ]