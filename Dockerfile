# Gunakan image Python ringan
FROM python:3.10-slim

# Atur working directory
WORKDIR /app

# Salin requirements dan instal dependensi
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode aplikasi
COPY . .

# Ekspose port aplikasi
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
