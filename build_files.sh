#!/bin/bash

# 1. Install dependensi
python3 -m pip install -r requirements.txt

# 2. Jalankan migrasi database ke Postgres Neon
python3 manage.py migrate --noinput

# 3. Kumpulkan file statis (opsional tapi disarankan untuk Vercel)
python3 manage.py collectstatic --noinput --clear