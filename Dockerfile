# استخدام إصدار بايثون مستقر
FROM python:3.12-slim

# ضبط متغيرات البيئة
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# تحديد مجلد العمل
WORKDIR /app

# تثبيت الاعتمادات
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# نسخ ملفات المشروع
COPY . /app/

# تشغيل التطبيق باستخدام daphne
CMD daphne socialMedia.asgi:application --port $PORT --bind 0.0.0.0