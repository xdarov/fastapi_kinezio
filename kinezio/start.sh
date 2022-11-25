export 'DB_ENGINE=***' \
    'DB_HOST=***' \
    'DB_DATABASE=***' \
    'DB_PORT=***' \
    'DB_USER=***' \
    'DB_PASSWORD=***'

uvicorn main:app --reload --port ***

# python database/get_db_settings.py
