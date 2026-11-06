FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Non-root user: if the container is compromised, the attacker does not get root
RUN addgroup --system app && adduser --system --ingroup app app

# Copy requirements first so the package layer is cached and builds stay fast
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER app

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
