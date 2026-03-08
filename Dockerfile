FROM python:3.10-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./
COPY src ./src

RUN uv sync --frozen

EXPOSE 8000

CMD ["uv", "run", "fastapi", "dev", "src/rails/main.py", "--host", "0.0.0.0", "--port", "8000"]
