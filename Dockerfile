FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
RUN uv pip install --system --no-cache .

COPY src/ ./src/

EXPOSE 8000

CMD ["uvicorn", "src.reservas.api:app", "--host", "0.0.0.0", "--port", "8000"]