#!/bin/bash

# 1. Install semua requirements
python3 -m pip install -r requirements.txt

# 2. Jalankan migrasi database ke Postgres Neon
python3 manage.py migrate --noinput