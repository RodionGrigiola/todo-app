FROM python:3.11-slim

WORKDIR /app

# sys deps
RUN apt-get update && apt-get install -y build-essential

# copying deps
COPY pyproject.toml uv.lock ./

RUN pip install uv

# install project deps
RUN uv sync

COPY . .

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]