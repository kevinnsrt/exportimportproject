import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'importexportproject.settings')

# Inisialisasi Django terlebih dahulu
django.setup()

# OTOMATIS JALANKAN MIGRASI SAAT VERCEL NYALA
try:
    print("Menjalankan migrasi database ke Neon Postgres...")
    call_command('migrate', interactive=False)
    print("Migrasi sukses!")
except Exception as e:
    print(f"Gagal menjalankan migrasi otomatis: {e}")

application = get_wsgi_application()