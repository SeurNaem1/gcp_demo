# 1️⃣ Dùng Python chính thức, nhẹ
FROM python:3.11-slim

# 2️⃣ Tắt tạo .pyc và bật log stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ Thư mục làm việc trong container
WORKDIR /app

# 4️⃣ Copy requirements trước để tận dụng cache
COPY requirements.txt .

# 5️⃣ Cài thư viện
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Copy toàn bộ source code
COPY . .

# 7️⃣ Cloud Run dùng cổng 8080
ENV PORT=8080

# 8️⃣ Chạy app bằng Gunicorn (chuẩn production)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
