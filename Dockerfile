FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# non-root user (container hack ho toh bhi root access nahi milega)
RUN addgroup --system app && adduser --system --ingroup app app

# pehle sirf requirements copy: packages ki layer cache ho jaati hai, build tez hota hai
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER app

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
