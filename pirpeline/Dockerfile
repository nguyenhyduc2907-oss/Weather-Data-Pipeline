FROM python:3.13.18
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock README.md ./
COPY src ./src
RUN uv sync --locked

COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]
