
gunicorn -w 4 -b 127.0.0.1:5000 -D --access-logfile ./logs/log main:app





